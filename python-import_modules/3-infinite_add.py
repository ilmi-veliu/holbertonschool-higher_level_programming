#!/usr/bin/python3
import sys

if __name__ == "__main__":
    adition = 0

    for i in range(1,len(sys.argv)):
        adition += int(sys.argv[i])
    
    print(adition)
