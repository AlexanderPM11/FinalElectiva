
from pydoc import cli
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client()
client.connect(mqttBroker)


def on_message(client, userData, msg):
    print("Recive: ", str(msg.payload.decode("utf-8")))


def example(color, location):
    datasJson = {
        "color": color,
        "meters": 1,
        "steps": 10,
        "location": location
    }
    client.publish("trafficlight", str(datasJson))
    print("Mensaje enviado: " + str(datasJson) +
          " para el topic trafficlight")
    time.sleep(1)


def run(color, location):
    client.loop_start()
    client.subscribe("trafficlight")
    client.on_message = on_message
    example(color, location)
    client.loop_stop()
