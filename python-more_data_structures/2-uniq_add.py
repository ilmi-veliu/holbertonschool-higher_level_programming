def uniq_add(my_list=[]):
    unique_values = set(my_list)  # enlève les doublons
    addition = 0

    for i in unique_values:
        addition += i

    return addition
