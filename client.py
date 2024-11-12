import random
import time

import paho.mqtt.client as mqtt

# MQTT configs
broker = "broker-mqtt"
port = 1883
topic = "sensor/temperature"

# Função para simular a temperatura
def simulate_temperature():
    # simula a temperatura entre 20 e 30 graus
    return round(random.uniform(20.0, 30.0), 2)

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

# MQTT on_message callback
def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload}")

# Create MQTT client and set callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Start the MQTT client loop
client.loop_start()

try:
    while True:
        # Simulate temperature and publish to the broker
        temperature = simulate_temperature()
        client.publish(topic, temperature)
        print(f"Published temperature: {temperature}°C")
        time.sleep(5)
except KeyboardInterrupt:
    print("Simulation stopped")

# Stop the MQTT client loop and disconnect
client.loop_stop()
client.disconnect()