from pwn import *

if __name__ == '__main__':
    #p = process(["python3", "main.py"])
    p = remote('localhost', 1239)
    while True:
        line = p.recvline().strip().decode("ascii")
        if line.startswith("What is "):
            qn = line[8:]
            print(qn)
            if "exit" in qn:
                continue
            ans = eval(qn)
            p.sendline(str(ans))
        elif "ctf" in line:
            print(line)
            break

