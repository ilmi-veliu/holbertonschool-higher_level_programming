#!/usr/bin/python3
def uppercase(str):
    str_MAJ = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            str_MAJ = str_MAJ + chr(ord(str[i]) - 32)
        else:
            str_MAJ = str_MAJ + str[i]
    print("{}".format(str_MAJ))
