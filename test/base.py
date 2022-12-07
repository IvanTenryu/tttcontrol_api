import json
import requests

# Add parent folder to path
import os
import sys
parent_folder = os.path.dirname(os.path.dirname(__file__))
sys.path.append (parent_folder)

# Import api port
from config.config import api_port

class ApiTest ():
    def __init__ (self, endpoints_base:str, endpoints:list):
        """Contructor of class

        Args:
            endpoints_base (str): main endpoint for the test group, like "user"
            endpoints (list): lists of dictionaries with endpoints details (url, info, method and data)
        """
        # Parameters
        self.endpoints_base = endpoints_base
        self.endpoints = endpoints

        # Create api base link
        self.api_base = f"http://localhost:{api_port}"
    
    def run_tests (self):

        # call each endpoint
        for endpoint in self.endpoints:

            # Get endpoint info
            url = f"{self.api_base}/{self.endpoints_base}/{endpoint['url']}"
            method = endpoint["method"]
            data = json.dumps(endpoint["data"], default=str)
            info = endpoint["info"]
            
            print (f"\nApi call: {url} ({info})")
            
            # Call in correct method
            res = None
            if method == "get":
                res = requests.get (url)
            else:
                res = requests.post (url, json=data)
            
            # Show api call results
            print (f"Response code: {res.status_code}")

            # Print json data or response, if exists
            try:
                json_data = res.json()
            except:
                pass
            else:
                print (f"Response content:")
                print (json_data)