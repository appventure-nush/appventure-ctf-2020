import subprocess
import time
from pwn import *

r = remote('35.185.183.51', 4200)

with open('tryflag','w') as f:
    while True:
        t = []
        try: 
            t.append(('start', time.time()))
            inputs = r.recvall()
            t.append(('got', time.time()))
            outputs = subprocess.check_output('./solution', input=inputs).decode('utf-8')
            t.append(('solved', time.time()))
            r.send(outputs)
            t.append(('replied', time.time()))
            f.write(inputs)
        except EOFError:
            print("TLE")
        finally:
            print(t)
