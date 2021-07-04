import subprocess

class HealthcheckPing:
    def __init__(self, host):
        self.host = host

    def isHealthy(self):        
        try:
            subprocess.check_output(["ping", "-c", "1", self.host])
            return True                      
        except subprocess.CalledProcessError:
            return False

if __name__ == "__main__":
    healthcheck = HealthcheckPing("example.org")
    print(healthcheck.host, healthcheck.isHealthy())             