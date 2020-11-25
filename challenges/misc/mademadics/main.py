import random
import time


ops = ["+", "-", "*", "%"]

if __name__ == '__main__':
    flag = open("flag.txt", "r").read()
    start = time.time()
    print("Answer 100 questions in 5 seconds and you'll get the flag")
    for x in range(100):
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        op = random.randint(0, 3)
        if op == 0:
            res = a + b
        elif op == 1:
            res = a - b
        elif op == 2:
            res = a * b
        else:
            res = a % b
        print(f"What is {a} {ops[op]} {b}")
        try:
            inp = int(input())
        except:
            print("That doesn't seem to be a number!\n\n")
            exit()
        if inp == res:
            print("Correct!\n\n")
        else:
            print("Incorrect!\n\n")
            exit()
        if time.time() - start > 5:
            print("Oh no, your time is up!")
            exit()
    #  Lol
    print("What is exit()")
    print("Here's your flag:", flag)
