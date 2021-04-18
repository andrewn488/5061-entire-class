"""
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
Assignment: P3: Quadratic - Newton_Raphson
Newton-Raphson for quadratic formula
Find x such that 'ax^2 + bx + c' is within epsilon of a*10e-10
10/4/2020
"""

import math
import random

# variables
print('solving ax^2 + bx + c = 0: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

initial_guess = random.randint(-100, 100)     # random initial guess
iterations = 0      # iteration accumulator
epsilon = a * 10**-10
# first successive approximation
guess = initial_guess - (a * initial_guess * initial_guess + b * initial_guess + c) / (2 * a * initial_guess + b)   

# calculation and loop
if b**2 >= 4 * a * c:
    quadratic = a * initial_guess * initial_guess + b * initial_guess + c     # quadratic
    while quadratic >= epsilon:
        guess = guess - (a * guess * guess + b * guess + c) / (2 * a * guess + b)   # second successive approximations and beyond
        quadratic = a * guess * guess + b * guess + c
        iterations += 1
else:
    print('STOP')
    
# output
print('initial guess is: ', initial_guess)
print('one root is: ', guess)
print('took', iterations, 'iterations')
