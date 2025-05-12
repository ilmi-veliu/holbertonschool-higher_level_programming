#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_2 = my_list[:]

    if idx < 0:
        return my_list_2
    if idx >= len(my_list):
        return my_list_2

    my_list_2[idx] = element
    return my_list_2
