import os
import socket

class HealthcheckPort:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def isHealthy(self):        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.port))
            s.shutdown(2)
            return True
        except:
            return False    

if __name__ == "__main__":
    healthcheck = HealthcheckPort("example.org", 80)
    print(healthcheck.host, healthcheck.port, healthcheck.isHealthy())             