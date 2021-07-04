import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class HealthcheckHTTP:
    def __init__(self, url):
        self.url = url
        self.verifySSL = os.getenv("VERIFY_SSL", 'true').lower() in ['true', '1']

    def isHealthy(self):
        try:
            response = requests.get(self.url, verify = self.verifySSL)
            return response.status_code == 200
        except:
            return False

if __name__ == "__main__":
    healthcheck = HealthcheckHTTP("http://example.org")
    print(healthcheck.url, healthcheck.isHealthy())             