# ZIP

When running `file out.zip`, we discover that it's actually a JAR file.
```shell script
$ file out.zip                                                                                                                            /d/github/appventure-ctf-2020/challenges/forensics/zip
out.zip: Java archive data (JAR)
```

However, running the JAR file produces an error.
```shell script
$ java -jar out.zip                                                                                                                       /d/github/appventure-ctf-2020/challenges/forensics/zip
no main manifest attribute, in out.zip
```
Instead of fixing the error by editing the manifest file in the JAR, we can unzip the file and run the main class directly.
```shell script
$ java Test
ctf{j4v4_j4r5_4r3_ju5t_z1p5}
```
