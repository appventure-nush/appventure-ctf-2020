#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libnum import *

p = 9313999108056993013
q = 9636322847872464473
n = p*q
l = lcm(p-1,q-1)
e = 2
while e < l:
    if gcd(e,l) == 1:
        break
    e += 1

m = "ctf{2_e4Sy_r5a}"
c = pow(s2n(m),e,n)

print('n=',n)
print('e=',e)
print('c=',c)

