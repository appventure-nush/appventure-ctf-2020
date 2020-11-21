# Table

Since we're given a plain image, the first thing we should try is to check if there's any hidden information. By trial-and-error or godly forensic skills, you may find that the `stepic` python library works:

```python
# steg!
from PIL import Image
import stepic

im = Image.open(path)
enc = stepic.decode(im)
print(enc)
```

This code will output a suspicious string of hex data: `41b7eb0d426ac60b000000003f81042e417ffd8b4337d70a0000000042fdcf174200428f00000000436809c142fdcf174200428f0000000041402bd43f81042e41d7da31000000004304e7cc`.

We're a bit stuck though, let's look back at the challenge description to see if there are more clues.

> "Walking into the mysterious lab, you are greeted by a bizarre sight: **balloons everywhere and a laptop, bunch of metal samples in oil and a random slab of pumice stone on the table**...what's going on? Curious, you walked closer to find a suspicious image on the screen."

What's special about balloons, metal samples in oil, and pumice stone? This tests your general knowledge skill than CS actually, but pumice stone should come to mind as something that floats on water. Hmm...balloons float too, and if you google a bit (or remember some Chemistry general knowledge) you should find out that alkali metals such as Sodium are kept in oil. And oh, they also happen to float. Clearly, "float" must be an important idea in this challenge.

And it is! If you inspect the hex string, you will realise that it is 152 digits long which is equivalent to 76 bytes. Floats are 4 bytes, so this may correspond to 19 float values, which seems possible as a flag length. Let's try interpreting these hex digits as float values.

```python
def hex_to_float(hexa):
    return struct.unpack('!f',struct.pack('!I', int(hexa, 16)))[0]

# decode
lst = [enc[i:i+8] for i in range(0,len(enc),8)]
lst = list(map(hex_to_float, lst))
print(lst)
```

This gives us a bunch of numbers: `[22.989770889282227, 58.69340133666992, 0.0, 1.0079400539398193, 15.99940013885498, 183.83999633789062, 0.0, 126.90447235107422, 32.064998626708984, 0.0, 232.03810119628906, 126.90447235107422, 32.064998626708984, 0.0, 12.010700225830078, 1.0079400539398193, 26.981538772583008, 0.0, 132.90545654296875]` . You may see it instantly, but if you don't, let's try to see how we can arrive at the final piece of the puzzle. Recall that we are given a periodic table as the challenge. Open it up and stare at it a bit. Do some numbers look familiar?

Yes! In fact, these numbers are the molar masses of elements! By manual decoding, or using a periodic table library, you can decode the flag. Note that zeroes are clearly invalid values, and if you were to decode the flag without including them they will appear to function as spaces. Hence, you can go ahead and replace them with `_`s.

```python
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
```

and get the final flag: `ctf{NaNi_HOW_IS_ThIS_CHAl_Cs}`.

If it feels very guessy, that's why it is a misc challenge and not a crypto challenge.

