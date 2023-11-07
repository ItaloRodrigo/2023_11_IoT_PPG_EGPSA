from paho.mqtt import client as mqtt

clientID = "Italo";
port = 1883;
broker = "mqtt.tago.io";
topic = "tago/data/post";

client = mqtt.Client(clientID);
client.connect(broker,port);

client.publish()