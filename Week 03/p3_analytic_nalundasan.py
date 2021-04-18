"""
Andrew Nalundasan
P3: Quadratic - Analytic
Question 1 on P3 Assignment
10/3/2020
"""

import math         # import math so can use math.sqrt for square root function

# variables
print('solving ax^2 + bx + c = 0: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# calculate

root_1 = (-b + math.sqrt((b**2) - (4 * a * c))) / 2 * a     # root_1 b + ... 

root_2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)     # root_2 = b - ...

# print output
print('roots: {} {}'.format(root_1, root_2))
