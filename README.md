# 🌡️ Temperature Simulator on MQTT

This project simulates real-time temperature data and publishes it over the **MQTT** protocol using Python. It's designed for testing and validating IoT platforms, dashboards, and message brokers without needing physical sensors.

---

## 🚀 Features

- Simulates dynamic temperature values
- Publishes messages to a configurable MQTT topic
- Adjustable frequency and randomness
- Ideal for IoT development, broker testing, and data pipelines

---

## 🔧 Requirements

- Python 3.7+
- MQTT broker (e.g., Mosquitto, HiveMQ, EMQX)
- Python packages:
  - `paho-mqtt`
  - `random`, `time`

Install dependencies:

```bash
pip install paho-mqtt
