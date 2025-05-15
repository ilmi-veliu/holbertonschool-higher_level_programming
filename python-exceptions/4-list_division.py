#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    nvx_list = []

    for i in range(list_length):
        try:
            nvx_list.append( my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
              nvx_list.append(0)
              print("division by 0")
        
        except TypeError:
            print("wrong type")

        except IndexError:
            print("out of range")
        
        finally:
            pass

    
    return nvx_list
