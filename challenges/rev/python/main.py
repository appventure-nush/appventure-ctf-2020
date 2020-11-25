from dis import dis


def add(ints):
    return [x + len(ints) - 50 for x in ints]


def add2(ints):
    return [x - 2 * 5 for x in ints]


def main(string):
    ints = [ord(x) for x in string]
    x = [x + 3 + y for x, y in zip(add(ints), add2(ints))]
    return bytes(x)


def reverse(bytes):
    length = len(bytes)
    # byte = x + 3 + y = c - 50 + length + 3 + c - 10
    # 2c = byte + 57 - length
    # c = (byte + 57 - length)//2
    out = ""
    for byte in bytes:
        c = (byte + 57 - length) // 2
        out += chr(c)
    return out


if __name__ == '__main__':
    print(dis(main))
    out = main("ctf{r4p1d_un5ch3dul3d_d154553mbly}")
    print(out)
    print(reverse(out))
