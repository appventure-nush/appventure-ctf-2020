import subprocess
import time
from pwn import *

r = remote('35.185.183.51', 4200)

for i in range(9):
    r.recvline()

while True:
    try:
        print(('start', time.time()))
        line = r.recvline().decode()
        inputs = line
        tc = int(line)

        for tci in range(tc):
            line = r.recvline().decode()
            inputs += line
            N, M, L = list(map(int, line.split()))
            for _ in range(L):
                line = r.recvline().decode()
                inputs += line

        print(('got', time.time()))
        outputs = subprocess.check_output('./solution', input=bytes(inputs, 'utf-8')).decode('utf-8')
        print(('solved', time.time()))
        r.send(outputs)
        print(('replied', time.time()))
        line = r.recvline().decode()
        print('reply=', line)
    except TypeError as e:
        print(e, 'error', line)

#lineno = 0
#with open('testcases/1.in') as f:
#    line = f.readline()
#    lineno += 1
#    #print(line)
#    inputs = line
#    tc = int(line)
#    for _ in range(tc):
#        line = f.readline()
#        lineno += 1
#        #print(line)
#        #print(line.strip())
#        inputs += line
#        N, M, L = list(map(int, line.split()))
#        for _ in range(L):
#            line = f.readline()
#            lineno += 1
#            inputs += line
#
#    print(lineno)
#    outputs = subprocess.check_output('./solution', input=bytes(inputs, 'utf-8')).decode('utf-8')
#    with open('testing.out', 'w') as f:
#        f.write(outputs)
