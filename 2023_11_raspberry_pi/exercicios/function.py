import sys
import time

def execute(arg1):
    try:
        teste()
        while True:
            print("aqui"+str(arg1))  
            time.sleep(5)  
    except KeyboardInterrupt:
        print("Crtl+c para parar")
        sys.exit(0)
        
def teste():
    print("olha")