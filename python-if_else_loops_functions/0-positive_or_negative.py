#!/usr/bin/python3

import random
nb = random.randint(-50 , 100)

if nb > 0 :
    print(nb,'is positive')

elif nb == 0 :
    print(nb,'is zero')

else:
    print(nb,'is negative')