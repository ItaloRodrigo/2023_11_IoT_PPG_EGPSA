import random
import sys
import time
import requests
import json
 
API_KEY = "TLXKQBRONR7HMOGL"


 
# headers = {
#     "Content-Type": "application/json; charset=utf-8",
#     "Device-Token": API_KEY,
#     "ssl": "false",
# }

try:
    while True:
        
        # data = [
        #     {"variable": "temperatura","value": random.randint(5,36)},
        #     {"variable": "umidade","value": random.randint(5,36)},
        # ]
        
        temperatura = random.randint(5,36)
        umidade = random.randint(0,100)
        
        url = "https://api.thingspeak.com/update?api_key="+API_KEY+"&field1="+str(temperatura)+"&field2="+str(umidade)
    
        response = requests.get(url)
        
        print("Temperatura:"+str(temperatura)+" - Umidade: "+str(umidade))
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())  
        time.sleep(15)  
except KeyboardInterrupt:
    print ("dfhfdh")
    sys.exit(0)

