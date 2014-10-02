import string
import os
import shutil

#subprocess.call("./home/user/src/proj1/files/deldirs.scr")

alphabet = string.ascii_lowercase

file_list = os.listdir("/home/user/src/proj1/files")

#make all the directories
for char in alphabet:
    os.mkdir(char)
for sortingfile in file_list:
    print sortingfile[0]
    print sortingfile
    shutil.move(sortingfile, sortingfile[0])