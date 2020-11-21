import pickle
import platform

if __name__ == '__main__':
    inp = input("""
Commands:
[0]: Print python version
[1]: Unpickle (hex)

Enter command number: """)
    try:
        if inp.strip() == "0":
            print("Python "+platform.python_version())
        elif inp.strip() == "1":
            pic = bytes.fromhex(input("Enter pickle: "))
            if b"flag" in pic:
                print("Banned!")
            else:
                pickle.loads(pic)
        else:
            print("Invalid input!")
    except:
        print("Something bad happened!")
        exit()
    print("Bye!")
