import os
import random
import shutil
import zipfile

if __name__ == '__main__':
    flag = open("flag.txt", "r").read()
    os.mkdir("./out")
    flag_num = random.randrange(0, 500)
    print(flag_num)
    # 310
    for i in range(1000):
        zf = zipfile.ZipFile('out.zip', 'w', zipfile.ZIP_DEFLATED)
        with open(f"./out/{i}.txt", "w") as file:
            if i == flag_num:
                file.write(flag)
            else:
                file.write("nope!")
        zf.write("out")
        if i != 0:
            zf.write("out/out.zip")
        zf.write(f"./out/{i}.txt")
        zf.close()
        os.unlink(f"./out/{i}.txt")
        shutil.copyfile("out.zip", "./out/out.zip")
