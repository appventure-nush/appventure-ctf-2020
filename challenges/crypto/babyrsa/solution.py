from libnum import *

n= 89752702410033356872624682474051727149
e= 5
c= 8569036008785673921403170186780173601
p = 9313999108056993013
q = 9636322847872464473
l = lcm(p-1,q-1)
d = invmod(e,l)

print(n2s(pow(c,d,n)))
