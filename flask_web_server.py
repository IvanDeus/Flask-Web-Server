# ivan deus 2025
import logging
from flask import Flask
from flask_web_server_cfg import WPORT, DEBUG, LOGFILE

app = Flask(__name__)
# Configure logging
# Log level based on DEBUG flag
logging.basicConfig(
    filename=LOGFILE,
    format='%(levelname)s: %(message)s',
    level=logging.INFO if not DEBUG else logging.DEBUG 
)
# Also log to console (especially useful during development)
if DEBUG:
    logging.getLogger().addHandler(logging.StreamHandler())
# Main web page
@app.route('/')
def index():
    logging.info("Index route accessed")
    return 'Place your files into /static directory'
# Run flask web app   
if __name__ == '__main__':
    logging.info("Starting Flask web server...")
    app.run(host='127.0.0.1', port=WPORT, debug=DEBUG)
