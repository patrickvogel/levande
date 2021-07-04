import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Healthcheck:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.verifySSL = os.getenv("VERIFY_SSL", 'true').lower() in ['true', '1']

    def isHealthy(self):
        try:
            response = requests.get(self.url, verify = self.verifySSL)
            return response.status_code == 200
        except:
            return False

if __name__ == "__main__":
    healthcheck = Healthcheck("Example", "http://example.org")
    print(healthcheck.name, healthcheck.isHealthy())             