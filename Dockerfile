FROM python:3.9-slim

WORKDIR /app

COPY client.py .


RUN pip install paho-mqtt 

CMD ["python", "client.py"]