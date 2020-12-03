import os
import sys
import signal
import random
import subprocess

# config
TC_NUMBER = 20
TIME_LIMIT = 5 + 120
FLAG = [
    "ctf{e45y_p3AsY_M4cH1n3_g0ES_8rRRr}",
    "ctf{SIMPl1c17y_I5_8eAU7iFuL}"
]
LIMIT = [
    200000,
    5000000
]
DEBUG = True

def generate_testcase(MAX_N, tight=False):
    N = MAX_N if tight else random.randint(1, MAX_N)
    inputs = "{}\n".format(N);
    for i in range(N):
        P = random.randint(0, 5000000)
        R = random.randint(0, 5000000)
        inputs += "{} {}\n".format(P,R)

    outputs = subprocess.check_output('./solution', input=bytes(inputs, 'utf-8')).decode('utf-8')
    #outputs = subprocess.check_output('./brute', input=bytes(inputs, 'utf-8')).decode('utf-8')
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
    print(FLAG[ST])


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
        yield generate_testcase(MAX_N=LIMIT[ST], tight=(idx > 10))
        idx += 1

if __name__ == "__main__":
    # setup
    signal.signal(signal.SIGALRM, time_limit_exceeded)
    display_banner()
    testcases = get_testcases(TC_NUMBER)

    while True:
        try:
            ST = int(input("Input subtask [1/2]: "))
            if ST < 1 or ST > 2:
                raise "Invalid input"
            break
        except:
            print("Invalid subtask")
            sys.exit(0)

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

