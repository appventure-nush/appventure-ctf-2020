import random
import string

import numpy as np
import pandas as pd


def encrypt(data):
    assert len(data) == 16
    matrix = [[ord(x) for x in data[i:i + 4]] for i in range(0, 16, 4)]
    df = pd.DataFrame(matrix)
    seed = data[5]
    random.seed(seed)
    for round_num in range(16):
        round_key = [np.array([random.randint(0, 100) + round_num for _ in range(4)]) for _ in range(4)]
        new_df = pd.DataFrame(np.zeros((4, 4)))
        df = df.rename(index={0: 3, 1: 2, 2: 0, 3: 1})
        for idx, row in df.iterrows():
            new_df[idx] = np.bitwise_xor(row, round_key[idx])
        df = new_df.T
    output = bytes()
    for idx, row in df.iterrows():
        output += bytes(row.tolist())
    return output.hex()


if __name__ == '__main__':
    # Implementation check:
    # 0123456789abcdef should encrypt to:
    # 642810404e6a3661336d787d5c76082d
    #
    # If it produces a different value, check with organizers
    inp = input("Enter text to encrypt: ")
    if len(inp) != 23:
        print("That is not the flag!")
    for i in inp:
        if i not in string.ascii_letters + string.digits + "_{}":
            raise Exception("Invalid characters")
    out = ""
    # Remember to remove padding when submitting flag
    blocks = [inp[i:i + 16].zfill(16) for i in range(0, len(inp), 16)]
    for block in blocks:
        out += encrypt(block)
    print(out)
    # Encrypted flag:
    # 684154740b2a2e2c3a7f164e344f75377d0e31581104692e307f247a1b175c51
