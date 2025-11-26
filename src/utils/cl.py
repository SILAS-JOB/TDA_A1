import os 
import time 

def clean():
    if os.name == 'nt':
        time.sleep(2)
        os.system('cls')
    else:
        time.sleep(2)
        os.system('clear')