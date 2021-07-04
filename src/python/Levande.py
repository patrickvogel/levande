import json
import os
from Healthcheck import Healthcheck

class Levande:
    def __init__(self):
        configFilePath = os.getenv("LEVANDE_CONFIG_FILE", 'config/levande.json')
        configFile = open(configFilePath)
        self.config = json.load(configFile)        

    def getStatus(self):
        status = []
        for system in self.config.get("systems"):
            healthcheck = Healthcheck(system.get("name"), system.get("url"))
            statusStr = os.getenv("LEVANDE_STATUS_DOWN", 'DOWN')
            if healthcheck.isHealthy():
                statusStr = os.getenv("LEVANDE_STATUS_UP", 'UP')
            status.append({ "id": system.get("id"), "name": system.get("name"), "status": statusStr })
        return status

if __name__ == "__main__":
    levande = Levande()
    print(levande.getStatus())       