# input config
path = "./chal.png"

# steg!
from PIL import Image
import stepic

im = Image.open(path)
enc = stepic.decode(im)
print(enc, len(enc))

# helpers
import struct

def float_to_hex(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '08x')

def hex_to_float(hexa):
    return struct.unpack('!f',struct.pack('!I', int(hexa, 16)))[0]

# decode
lst = [enc[i:i+8] for i in range(0,len(enc),8)]
lst = list(map(hex_to_float, lst))
print(lst)

# identify the elements!
from periodictable import elements

flag = ""
for x in lst:
    hit = False
    for el in elements:
        if abs(x-el.mass) < 1e-4:
            flag += el.symbol
            hit = True
            break
    if not hit:
        flag += "_"
print("ctf{%s}" % flag)
