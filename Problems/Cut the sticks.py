import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    sticks = []
    arr.sort()
    len_arr = len(arr)

    while len_arr > 0:
        sticks.append(len_arr)
        min = arr[0]
        arr = [x-min for x in arr]
        arr = [x for x in arr if x]
        len_arr = len(arr)

    return sticks

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))