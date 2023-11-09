import paho.mqtt.client as mqtt
import sys
import random
import time
import json

class Mqtt:
    # Definicoes:
    device_token = "75d1e803-d751-4372-84e5-dd92025d54eb" #device token do seu dispositivo
    broker = "mqtt.tago.io"
    porta_broker = 1883
    keep_alive_broker = 60
    timeout_conexao = 15 # Timeout da conexao com broker MQTT
    topico_publish = "tago/data/post"
    mqtt_username = "dispositivo_iot_curso" # Um nome qualquer
    mqtt_password = device_token
    temperatura = 0
    pressao = 0
    umidade = 0
    
    def __init__(self, temperatura, pressao, umidade):
        self.temperatura = temperatura
        self.pressao = pressao
        self.umidade = umidade

    # Callback - conexao ao Broker realizada
    def on_connect(self,client, userdata, flags, rc):
        print ("[STATUS] Conectado ao Broker. Resultado de conexao: " + str(rc)) 
        
        #faz subscribe automatico no topico
        client.subscribe(self.topico_publish)

    def main(self):
        # Programa principal
        try:
            print ("[STATUS] Inicializando MQTT...") 
            client = mqtt.Client('teste') #inicializa MQTT:
            client.username_pw_set(self.mqtt_username, self.mqtt_password)
            client.on_connect = self.on_connect
            client.connect(self.broker, self.porta_broker, self.keep_alive_broker)
            
            status_conexao_broker_tago_io = client.loop(self.timeout_conexao)
            if (status_conexao_broker_tago_io > 0):
                client.connect(self.broker, self.porta_broker, self.keep_alive_broker)
        
            # Gera temperatura e umidade aleatorias
            # temperatura = random.randint(5,36)
            # umidade = random.randint(20,60)

            # Envia dados corretamente formatados para o tago.io
            client.publish(self.topico_publish, json.dumps({"variable": "temperatura", "unit": "C", "value": self.temperatura}))
            client.publish(self.topico_publish, json.dumps({"variable": "pressao", "unit": "mbar", "value": self.pressao})) 
            client.publish(self.topico_publish, json.dumps({"variable": "umidade", "unit": "%", "value": self.umidade}))
            
            print("enviado!")

        # Encerramento do programa (pressiona CTRL+C)
        except KeyboardInterrupt:
            print  ("\nCtrl+C pressionado, encerrando aplicacao e saindo...") 
            sys.exit(0)