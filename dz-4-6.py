from itertools import count
from itertools import cycle

my_list = count(5)
for el in my_list:
    while el < 8:
        print(el)
        el += 1


i = 0
for el in cycle(my_list):
    while i < 9:
    print(el)
    a += 1


