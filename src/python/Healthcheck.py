import requests

class Healthcheck:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def isHealthy(self):
        try:
            response = requests.get(self.url)
            return response.status_code == 200
        except:
            return False

if __name__ == "__main__":
    healthcheck = Healthcheck("Example", "http://example.org")
    print(healthcheck.name, healthcheck.isHealthy())             