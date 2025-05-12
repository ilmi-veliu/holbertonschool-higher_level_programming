#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for i, nombre in enumerate(ligne):
            if i == len(ligne) - 1:
                print("{:d}".format(nombre), end="")
            else:
                print("{:d}".format(nombre), end=" ")
        print()
