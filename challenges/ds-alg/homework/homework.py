import os
import sys
import signal
import random
import subprocess

# config
TC_NUMBER = 10
TIME_LIMIT = 5 + 10
FLAG = "ctf{n0w_gO_d0_yOuR_hom3w0rk!}"
DEBUG = False

def solve(inputs):
    outputs = ""
    tc = inputs[0]
    for idx, case in enumerate(inputs[1]):
        N, M, L = case[:3]
        v = []
        for i in range(L):
            name, a, b = case[3][i]
            x, y = N, M
            cost = 0
            while x > y:
                if x//2 >= y:
                    dec = x - x//2;
                    cost += min(dec*a, b);
                    x //= 2;
                else:
                    cost += (x-y)*a;
                    x = y;
            v.append((cost,name))
        v.sort()

        outputs += "Case {}\n".format(idx+1)
        for x in v:
            outputs += "{} {}\n".format(x[1], x[0])
    return outputs

def generate_testcase():
    tc = random.randint(1,250);
    inputs = "{}\n".format(tc)

    inputs_raw = []
    for _ in range(tc):
        N = random.randint(1, 100000)
        M = random.randint(1, 100000)
        if N < M:
            N, M = M, N
        L = random.randint(1, 100)
        inputs += "{} {} {}\n".format(N, M, L);

        lines = []
        for i in range(L):
            name = ''.join([chr(random.randint(ord('A'), ord('Z'))) for _ in range(random.randint(1,16))])
            A = random.randint(0, 10000)
            B = random.randint(0, 10000)
            inputs += "{}:{},{}\n".format(name, A, B);
            lines.append((name, A, B)) 

        inputs_raw.append((N, M, L, lines))

    #return inputs, solve((tc, inputs_raw))
    outputs = subprocess.check_output('./solution', input=bytes(inputs, 'utf-8')).decode('utf-8')
    return inputs, outputs


# template
# verdicts
def time_limit_exceeded(signum, stack_frame):
    print("[TLE] Too slow!")
    sys.exit(0)


def wrong_answer():
    print("[WA] Wrong!")
    sys.exit(0)


def accepted():
    print("[AC] Accepted.")


# ctf things
def win():
    print("Congrats! Here is your flag:")
    print(FLAG)


def display_banner():
    print("""
______  _____         ___   _     _____
|  _  \/  ___|       / _ \ | |   |  __ \\
| | | |\ `--. ______/ /_\ \| |   | |  \/
| | | | `--. \______|  _  || |   | | __
| |/ / /\__/ /      | | | || |___| |_\ \\
|___/  \____/       \_| |_/\_____/\____/

    """)


def get_testcases(n):
    # fixed
    fixed = list(filter(lambda x: x[-3:] == '.in', os.listdir('./testcases')))
    random.shuffle(fixed)

    idx = 0
    if idx < len(fixed):
        name = fixed[idx][:-3]
        with open('./testcases/{}.in'.format(name), 'r') as f:
            inputs = f.read()
        with open('./testcases/{}.out'.format(name), 'r') as f:
            outputs = f.read()
        yield inputs, outputs
        idx += 1

    while idx < n:
        yield generate_testcase()
        idx += 1

if __name__ == "__main__":
    # setup
    signal.signal(signal.SIGALRM, time_limit_exceeded)
    display_banner()
    testcases = get_testcases(TC_NUMBER)

    # grading
    for tc in testcases:
        print(tc[0])
        signal.alarm(TIME_LIMIT)

        if DEBUG:
            response = subprocess.check_output('./solution', input=bytes(tc[0], 'utf-8')).decode('utf-8')
        else:
            response = input()

        signal.alarm(0)
        if response.strip() == tc[1].strip():
            accepted()
        else:
            wrong_answer()
    win()

