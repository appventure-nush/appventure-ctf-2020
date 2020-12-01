from dis import dis


def a(ints):
    return [x + len(ints) - 50 for x in ints]


def b(ints):
    return [x - 2 * 5 for x in ints]


def c(string):
    ints = [ord(x) for x in string]
    x = [x + 3 + y for x, y in zip(a(ints), b(ints))]
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
    print("Function A:")
    dis(a)
    print("Function B:")
    dis(b)
    print("Function C:")
    dis(c)
    out = c("ctf{r4p1d_un5ch3dul3d_d154553mbly}")
    print(out.hex())
    print(reverse(out))
