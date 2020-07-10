from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

n = fact()
x = 0
for i in n:
    if x < 15:
        print(i)
        x += 1
    else:
        break