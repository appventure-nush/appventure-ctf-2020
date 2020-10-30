import random
import string
from binascii import a2b_hex

import numpy as np


def decrypt(enc, seed):
    random.seed(seed)
    ints = [x for x in a2b_hex(enc)]
    assert len(ints) == 16
    out_matrix = [ints[i:i + 4] for i in range(0, 16, 4)]
    rounds = 16
    round_keys = [[np.array([random.randint(0, 100) + round_num for _ in range(4)]) for _ in range(4)] for round_num in
                  range(rounds)]
    round_keys = round_keys[::-1]
    for round_num in range(rounds):
        dec_matrix = []
        for i in [3, 2, 0, 1]:
            dec_matrix.append(np.bitwise_xor(out_matrix[i], round_keys[round_num][i]))
        out_matrix = dec_matrix
    dec = ""
    for row in out_matrix:
        for col in row:
            dec += chr(col)
    return dec


def decrypt2():
    inp = "261e663a111115760b5d216f4e7a253f7d0e31581104692e6e763f6f074c0851"
    decrypted = ""
    blocks = [inp[i:i + 32] for i in range(0, len(inp), 32)]
    for seed in string.ascii_letters + string.digits + "_{}":
        dec = decrypt(blocks[0], seed)
        if dec.startswith("ctf"):
            decrypted += dec
            break
    decrypted += decrypt(blocks[1], "0")
    print(decrypted)


if __name__ == '__main__':
    decrypt2()
