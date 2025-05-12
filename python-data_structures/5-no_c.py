#!/usr/bin/python3
def no_c(my_string):
    string_2 = my_string[:]

    for i in range (len(my_string)):
        if string_2[i] == "c" or string_2[i] == "C":
            string_2 = string_2.replace("c","C")
            return string_2
