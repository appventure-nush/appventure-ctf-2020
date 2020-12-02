import glob
import os
import shutil
import zipfile

if __name__ == '__main__':
    os.mkdir("out")
    i = 0
    while True:
        with zipfile.ZipFile("./out.zip", 'r') as zip_ref:
            zip_ref.extractall("./out")
        with open(glob.glob("./out/out/*.txt")[0], "r") as file:
            content = file.read()
            if "ctf" in content:
                print(content, i)
                break
        shutil.copyfile("./out/out/out.zip", "./out.zip")
        shutil.rmtree("./out/out")
        i += 1
