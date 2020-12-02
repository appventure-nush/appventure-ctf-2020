import random

random.seed(1382190839)

s = 'ctf{i_s4iD_f4st3rrRRr}'
l = []
for i in range(491-len(s)): l.append((-1,random.randint(ord('A'),ord('z'))))

p = 101
q = 403
m = len(l)
r = 0
seq = []
inv = []
for i in range(len(s)):
    r = (r*p + q) % m
    seq.append((r, i))
    inv.append(r)

seq.sort()
for x in seq:
    l.insert(x[0], (x[1],ord(s[x[1]])))

print(list(map(lambda x: x[1], l)))
print(p, q, m)
print((r*p + q) % m)
print(inv)
