# output config
path = "./chal.png"

import struct

# helpers
def float_to_hex(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '08x')

def hex_to_float(hexa):
    return struct.unpack('!f',struct.pack('!I', int(hexa, 16)))[0]

# encode flag
from periodictable import elements

elem = ["Na", "Ni", "_", "H", "O", "W", "_", "I", "S", "_", "Th", "I", "S", "_", "C", "H", "Al", "_", "Cs"]
flag = "ctf{" + ''.join(elem) + "}"
print("Created flag:", flag)

mass = []
for e in elem:
    mass.append(0 if e == "_" else elements.symbol(e).mass)

enc = ''.join(list(map(float_to_hex, mass)))
print("Generated encoded data:", enc)

# download image
import requests
import os
from PIL import Image

url = "https://iupac.org/wp-content/uploads/2018/12/IUPAC_Periodic_Table-01Dec18.jpg"
download = "./chal.jpg"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # fake a user agent so we can download
r = requests.get(url, headers=headers)
with open(download, "wb") as f:
    f.write(r.content)
print("Downloaded source image: ", download)

im = Image.open(download)

# steg!
import stepic

stepic.encode(im, bytes(enc, "utf-8")).save(path)
print("Written stegged image to ", path)

# clean up
os.remove(download) # clean up
print("Cleaned up intermediate files.")
