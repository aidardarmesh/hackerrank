# a 3 => d
# A 3 => D

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    result = ''
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')

    for ch in s:
        ch = ord(ch)

        if a <= ch <= z:
            delta = ch - a
            delta = (delta + k) % 26
            ch = a + delta
        elif A <= ch <= Z:
            delta = ch - A
            delta = (delta + k) % 26
            ch = A + delta

        result += chr(ch)

    return result

if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result)
