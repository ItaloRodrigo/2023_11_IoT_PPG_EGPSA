#Programa: simulador de dispositivo IoT.
#          Plataforma IoT usada: Tago.io
#Autor: Ítalo Rodrigo
#

import paho.mqtt.client as mqtt
import sys
import random
import time
import json

# Definicoes:
device_token = "75d1e803-d751-4372-84e5-dd92025d54eb" #device token do seu dispositivo
broker = "mqtt.tago.io"
porta_broker = 1883
keep_alive_broker = 60
timeout_conexao = 15 # Timeout da conexao com broker MQTT
topico_publish = "tago/data/post"
mqtt_username = "dispositivo_iot_curso" # Um nome qualquer
mqtt_password = device_token

# Callback - conexao ao Broker realizada
def on_connect(client, userdata, flags, rc):
    print ("[STATUS] Conectado ao Broker. Resultado de conexao: " + str(rc)) 
    
    #faz subscribe automatico no topico
    client.subscribe(topico_publish)

# Programa principal
try:
    print ("[STATUS] Inicializando MQTT...") 
    client = mqtt.Client('teste') #inicializa MQTT:
    client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.connect(broker, porta_broker, keep_alive_broker)
    
    status_conexao_broker_tago_io = client.loop(timeout_conexao)
    if (status_conexao_broker_tago_io > 0):
        client.connect(broker, porta_broker, keep_alive_broker)
 
    # Gera temperatura e umidade aleatorias
    temperatura = random.randint(5,36)
    umidade = random.randint(20,60)

    # Envia dados corretamente formatados para o tago.io
    client.publish(topico_publish, json.dumps({"variable": "temperatura", "unit": "C", "value": temperatura}))
    client.publish(topico_publish, json.dumps({"variable": "umidade", "unit": "%", "value": umidade})) 
    
    print("enviado!")

# Encerramento do programa (pressiona CTRL+C)
except KeyboardInterrupt:
    print  ("\nCtrl+C pressionado, encerrando aplicacao e saindo...") 
    sys.exit(0)
