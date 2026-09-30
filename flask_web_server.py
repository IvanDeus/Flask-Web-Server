# flask_web_server.py // ivan deus 2025/2026
import logging
import os
import socket
import sys
from flask import Flask, send_from_directory
def _env(name, default):
    return os.environ.get('FWS_' + name, default)
def _as_bool(value):
    return str(value).strip().lower() in ('1', 'true', 'yes', 'on')
def _as_port(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise SystemExit(f"Invalid port {value!r}: set FWS_PORT to a number")

HOST = _env('HOST', '0.0.0.0')
WPORT = _as_port(_env('PORT', '1555'))
DEBUG = _as_bool(_env('DEBUG', ''))
LOGFILE = _env('LOGFILE', 'flask_web_server.log')
NGROK_DOMAIN = _env('NGROK_DOMAIN', '')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# send_file resolves a relative directory against app.root_path, not cwd, so pin it at startup
STATIC_DIR = os.path.abspath(_env('STATIC', os.path.join(APP_ROOT, 'static')))

def _local_ip():
    # no packets are sent, this only asks the kernel which interface would reach the internet
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(('8.8.8.8', 80))
        return probe.getsockname()[0]
    except OSError:
        return '127.0.0.1'
    finally:
        probe.close()

def connect_ngrok():
    # Ngrok is optional: only touched when NGROK_AUTHTOKEN is set, so the import stays inside
    if not os.environ.get('NGROK_AUTHTOKEN'):
        return
    try:
        import ngrok
    except ImportError:
        logging.warning("NGROK_AUTHTOKEN is set but the 'ngrok' package is missing (pip install ngrok); continuing without a tunnel")
        return
    kwargs = {'authtoken_from_env': True}
    if NGROK_DOMAIN:
        kwargs['domain'] = NGROK_DOMAIN
    try:
        forwarder = ngrok.forward(f'localhost:{WPORT}', **kwargs)
    except Exception as err:
        # ngrok reports its own failures as a tuple, so str() it instead of letting a traceback out
        logging.error(f"Ngrok tunnel failed: {err} -- continuing without a tunnel")
        return
    logging.info(f"Ngrok tunnel: {forwarder.url()}")
# Flask's own /static rule would otherwise take precedence over send_static below
app = Flask(__name__, static_folder=None)
# Log level based on DEBUG flag; every record goes to both the log file and the console
logging.basicConfig(
    format='%(levelname)s: %(message)s',
    level=logging.DEBUG if DEBUG else logging.INFO,
    handlers=[
        logging.FileHandler(LOGFILE),
        logging.StreamHandler(sys.stdout),
    ],
)

@app.route('/')
def index():
    logging.info("Index route accessed")
    # Check if index.html exists in the static directory
    if os.path.exists(os.path.join(STATIC_DIR, 'index.html')):
        return send_from_directory(STATIC_DIR, 'index.html')
    return 'index.html not found. Place your files into /static directory'
# Serve any other file in /static automatically
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(STATIC_DIR, path)

if __name__ == '__main__':
    logging.info(f"Starting Flask web server on {HOST}:{WPORT}...")
    if HOST in ('0.0.0.0', '', '::'):
        print(f"IP:PORT {_local_ip()}:{WPORT} (also reachable as 127.0.0.1:{WPORT})")
    else:
        print(f"IP:PORT {HOST}:{WPORT}")
    connect_ngrok()
    app.run(host=HOST, port=WPORT, debug=DEBUG)
