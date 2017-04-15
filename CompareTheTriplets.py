"""
https://www.hackerrank.com/challenges/compare-the-triplets
"""

#!/bin/python3

import sys

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
# Write Your Code Here

"""
alice = 0
bob = 0
def cmpr(a,b):
    global alice
    global bob
    if a > b:
        alice += 1
    elif b > a:
        bob += 1

cmpr(a0,b0)
cmpr(a1,b1)
cmpr(a2,b2)

print(alice,bob)
"""

a = [a0,a1,a2]
b = [b0,b1,b2]
def score(a, b):
    alice = 0
    bob = 0
    i = 0
    while (i < len(a)):
        if (a[i] > b[i]):
            alice += 1
        elif (b[i] > a[i]):
            bob += 1
        i += 1
    print(alice, bob)
score(a, b)