# flask_web_server.py // ivan deus 2025/2026
import logging
import os
from flask import Flask, send_from_directory
from flask_web_server_cfg import HOST, WPORT, DEBUG, LOGFILE

app = Flask(__name__)
# Log level based on DEBUG flag
logging.basicConfig(
    filename=LOGFILE,
    format='%(levelname)s: %(message)s',
    level=logging.INFO if not DEBUG else logging.DEBUG 
)
if DEBUG:
    logging.getLogger().addHandler(logging.StreamHandler())
# Path where your static files live
STATIC_DIR = os.path.join(os.getcwd(), 'static')

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
    app.run(host=HOST, port=WPORT, debug=DEBUG)
