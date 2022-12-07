from app import app 
from config.config import api_debug, api_host, api_port

# Run app
if __name__ == '__main__':
    app.run (debug=api_debug, host=api_host, port=api_port)