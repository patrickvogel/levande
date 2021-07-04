import json
import os
from HealthcheckHTTP import HealthcheckHTTP
from HealthcheckPort import HealthcheckPort

class Levande:
    def __init__(self):
        configFilePath = os.getenv("LEVANDE_CONFIG_FILE", 'config/levande.json')
        configFile = open(configFilePath)
        self.config = json.load(configFile)        

    def getStatus(self):
        status = []
        for system in self.config.get("systems"):
            healthcheck = None
            if system.get("method") == "HTTP":
                healthcheck = HealthcheckHTTP(system.get("url"))
            if system.get("method") == "Port":
                healthcheck = HealthcheckPort(system.get("host"), system.get("port"))
            
            statusStr = os.getenv("LEVANDE_STATUS_DOWN", 'DOWN')
            if healthcheck.isHealthy():
                statusStr = os.getenv("LEVANDE_STATUS_UP", 'UP')
            status.append({ "id": system.get("id"), "status": statusStr })
        return status

if __name__ == "__main__":
    levande = Levande()
    print(levande.getStatus())       