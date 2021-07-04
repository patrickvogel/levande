import random
import time
import datetime
import os
from paho.mqtt import client as mqtt_client
from Levande import Levande

broker = os.getenv("MQTT_BROKER_HOST", '127.0.0.1')
port = int(os.getenv("MQTT_BROKER_PORT", '1883'))
topic_prefix = os.getenv("MQTT_TOPIC_PREFIX", 'levande/')
sleep = int(os.getenv("SLEEP_TIME", '30'))
client_id = os.getenv("MQTT_CLIENT_ID", f'python-mqtt-{random.randint(0, 1000)}')
username = os.getenv("MQTT_USERNAME", None)
password = os.getenv("MQTT_PASSWORD", None)


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    while True:
        levande = Levande()
        for system in levande.getStatus():            
            client.publish(topic_prefix+system.get("id"), system.get("status"))

        client.publish(topic_prefix+"lastUpdate", str(datetime.datetime.now()))

        time.sleep(sleep)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
