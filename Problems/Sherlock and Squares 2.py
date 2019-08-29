#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    # rootA is integer root of a (lower bound)
    # rootB is integer root of b (upper bound)
    # each integer between rootA and rootB can make up full square in range [a, b]
    # number of these full squares is b - a + 1
    # one added, because we count numbers in range

    # [3, 9], 3 - 2 + 1 = 2
    # [17, 24], 4 - 5 + 1 = 0

    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1

if __name__ == '__main__':
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    result = squares(a, b)

    print(result)