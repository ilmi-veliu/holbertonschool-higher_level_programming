#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = my_list[0]

    for nombre in my_list:
        if nombre > max_val:
            max_val = nombre

    return max_val
