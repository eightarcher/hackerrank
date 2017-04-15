"""
https://www.hackerrank.com/challenges/a-very-big-sum
"""

#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def summer(ray):
    toats = 0
    for num in ray:
        toats = toats + num
    print(toats)

summer(arr)
