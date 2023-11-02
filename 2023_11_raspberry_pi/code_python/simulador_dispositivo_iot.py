#Programa: simulador de dispositivo IoT.
#          Plataforma IoT usada: Tago.io
#Autor: Ítalo Rodrigo
#
#Importante: rode o script utilizando Python 2.x:
#python simulador_dispositivo_iot.py

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
    client = mqtt.Client() #inicializa MQTT:
    client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.connect(broker, porta_broker, keep_alive_broker)
    
    while True:
        # Garante a reconexao ao broker caso esta caia
        status_conexao_broker_tago_io = client.loop(timeout_conexao)
        if (status_conexao_broker_tago_io > 0):
            client.connect(broker, porta_broker, keep_alive_broker)
 
        # Gera temperatura e umidade aleatorias
        temperatura = random.randint(5,36)
        umidade = random.randint(20,60)
        print ("Temperatura gerada: " + str(temperatura) + "C") 
        print ("Umidade gerada: " + str(umidade) + "%") 
            
        # Prepara a formatacao dos dados coletados
        temperatura_json = {"variable": "temperatura", "unit": "C", "value": temperatura}
        umidade_json = {"variable": "umidade", "unit": "%", "value": umidade}
        temperatura_json_string = json.dumps(temperatura_json)
        umidade_json_string = json.dumps(umidade_json)
            
        # Envia dados corretamente formatados para o tago.io
        client.publish(topico_publish, temperatura_json_string)
        client.publish(topico_publish, umidade_json_string)

        # Aguarda 05 segundos para proximo envio a plataforma IoT
        time.sleep(5)

# Encerramento do programa (pressiona CTRL+C)
except KeyboardInterrupt:
    print  ("\nCtrl+C pressionado, encerrando aplicacao e saindo...") 
    sys.exit(0)
