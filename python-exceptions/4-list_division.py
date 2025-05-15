#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    nvx_list = []

    for i in range(list_length):
        try:
            nvx_list.append( my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
              nvx_list.append(0)
    
    return nvx_list
