import multiprocessing as mp
import os
import re


def check_safe_dir(account):
    safe_dir = os.path.realpath("./state/")
    if os.path.commonprefix((os.path.realpath(f"state/{account}.txt"), safe_dir)) != safe_dir:
        return False
    return True


def get_data(account):
    if not check_safe_dir(account):
        return
    with open(f"state/{account}.txt", "r") as f:
        return list(map(int, f.read().split(",")))


def write_data(account, bank, flags):
    if not check_safe_dir(account):
        return
    with open(f"state/{account}.txt", "w") as f:
        return f.write(",".join([str(bank), str(flags)]))


def buy_flag(account):
    bank, flags = get_data(account)
    if bank > 0:
        write_data(account, bank - 100, flags + 1)
        print(f"Bought flag! You have {flags + 1} flags!")
        if flags == 9:
            print("Flag")
    else:
        print("You're out of money!")
        os.remove(f"state/{account}.txt")


def donate(account):
    bank, _ = get_data(account)
    pattern = re.compile("^([a-zA-Z]+)*$")
    if not pattern.match(account):
        print("Invalid account name")
    _, flags = get_data(account)
    write_data(account, bank - 1, flags)
    print("Thank you for your donation!")


if __name__ == '__main__':
    print("Welcome to Quicc Bank!")
    account = input("Enter account name: ")
    print(f"Welcome, {account}. Valid commands are donate and buy")
    commands = input("Enter commands, separated by commas: ").split(",")
    # Many thread, such fast
    pool = mp.Pool(mp.cpu_count())
    write_data(account, 900, 0)
    for i in range(len(commands) - 1):
        if commands[i] == "donate":
            pool.apply_async(donate, args=[account])
        elif commands[i] == "buy":
            pool.apply(buy_flag, args=[account])
    pool.close()
    pool.join()
    # Oops, missed out last command
    if commands[-1] == "donate":
        donate(account)
    elif commands[-1] == "buy":
        buy_flag(account)
    os.remove(f"state/{account}.txt")
