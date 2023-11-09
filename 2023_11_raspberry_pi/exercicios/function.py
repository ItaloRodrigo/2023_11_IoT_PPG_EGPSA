import sys

def execute(arg1):
    try:
        while True:
            print("aqui"+str(arg1))    
    except KeyboardInterrupt:
        print("Crtl+c para parar")
        sys.exit(0)
        
