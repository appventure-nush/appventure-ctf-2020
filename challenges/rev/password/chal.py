import re


def check(password):
    assert re.match('^ctf{[a-z_]{16}}$', password)
    password = [ord(x) for x in password]
    return password[9] ^ password[19] == 58 and \
           password[4] ^ password[1] == 7 and \
           password[6] ^ password[18] == 2 and \
           password[4] ^ password[2] == 21 and \
           password[19] ^ password[0] == 6 and \
           password[1] ^ password[7] == 6 and \
           password[18] ^ password[17] == 17 and \
           password[15] ^ password[7] == 20 and \
           password[6] ^ password[1] == 21 and \
           password[4] ^ password[5] == 30 and \
           password[4] ^ password[20] == 14 and \
           password[12] ^ password[19] == 16 and \
           password[11] ^ password[16] == 29 and \
           password[2] ^ password[16] == 9 and \
           password[6] ^ password[10] == 3 and \
           password[4] ^ password[2] == 21 and \
           password[17] ^ password[9] == 45 and \
           password[4] ^ password[19] == 22 and \
           password[13] ^ password[20] == 9 and \
           password[11] ^ password[19] == 23


if __name__ == '__main__':
    password = input("Enter password: ")
    if check(password):
        print("Great! The flag is " + password)
    else:
        print("Wrong password")
