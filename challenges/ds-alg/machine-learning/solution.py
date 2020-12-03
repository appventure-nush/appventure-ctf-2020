import subprocess
import time
from pwn import *

r = remote('35.185.183.51', 4201)

for i in range(9):
    r.recvline()

print(r.recv())
r.sendline('1')

while True:
    try:
        print(('start', time.time()))
        line = r.recvline().decode()
        print('start', line)
        inputs = line
        N = int(line)

        for _ in range(N):
            line = r.recvline().decode()
            inputs += line

        print(('got', time.time()))
        outputs = subprocess.check_output('./solution', input=bytes(inputs, 'utf-8')).decode('utf-8')
        print(('solved', time.time()))
        r.send(outputs)
        print(('replied', time.time()))
        line = r.recvline().decode()
        line = r.recvline().decode()
        print('reply=', line)
    except TypeError as e:
        print(e, 'error', line)
