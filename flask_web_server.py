import logging
from flask import Flask
from flask_web_server_cfg import WPORT, DEBUG, LOGFILE

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename=LOGFILE,                  # Log output file
    format='%(levelname)s: %(message)s',  # Format of each log entry
    level=logging.INFO if not DEBUG else logging.DEBUG  # Log level based on DEBUG flag
)

# Optional: Also log to console (especially useful during development)
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
