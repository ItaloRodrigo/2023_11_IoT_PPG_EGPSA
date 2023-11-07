from paho.mqtt import client as mqtt;
import time;
import sys;

clientID = "dispositivo_iot_curso";
port = 1883;
broker = "mqtt.tago.io";
timeout_conexao = 15;
mqtt_username = "dispositivo_iot_curso"; # Um nome qualquer
mqtt_password = "75d1e803-d751-4372-84e5-dd92025d54eb";
topic = "tago/data/post";

def on_connect(client, userdata, flags, rc):
    print ("[STATUS] Conectado ao Broker. Resultado de conexao: " + str(rc)) 
    
    #faz subscribe automatico no topico
    client.subscribe(topic);
    
def on_message(client, userdata, message):
    print(f"Received: "+str(message.payload.decode("utf-8")))
    print("Topic: "+str(message.topic));

try:
    client = mqtt.Client(clientID);
    client.username_pw_set(mqtt_username, mqtt_password);
    client.on_connect = on_connect;
    client.connect(broker, port,60);

    while True:
        status = client.loop(timeout_conexao);
        if (status > 0):
            client.connect(broker, port, 60);
        client.subscribe(topic);
        client.on_message = on_message; 
        time.sleep(5);
except KeyboardInterrupt:
    print  ("\nCtrl+C pressionado, encerrando aplicacao e saindo...") 
    sys.exit(0)
    