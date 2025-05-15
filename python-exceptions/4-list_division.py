#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    nvx_list = []

    for i in range(list_length):
        try:
            nvx_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            nvx_list.append(0)
        except TypeError:
            print("wrong type")
            nvx_list.append(0)
        except IndexError:
            print("out of range")
            nvx_list.append(0)
        finally:
            pass

    return nvx_list
