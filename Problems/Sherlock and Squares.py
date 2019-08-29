#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    # squaresNumber = 0
    # get sqrt(a) and ceil it. It will be lower bound of roots
    # get sqrt(b) and floor it. It will be upper bound of roots
    # range through rootBounds by 1 and calculate square(each)
    # if square is in [a, b]
    # then squaresNumber += 1
    # return squaresNumber

    squares_number = 0
    lower_root = math.floor(math.sqrt(a))
    upper_root = math.ceil(math.sqrt(b))

    for i in range(lower_root, upper_root+1):
        if a <= i ** 2 <= b:
            squares_number += 1
    
    return squares_number

if __name__ == '__main__':
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    result = squares(a, b)

    print(result)