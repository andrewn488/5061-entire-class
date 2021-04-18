"""
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
Assignment: P3: Quadratic - Bisection
Bisection for quadratic formula
10/4/2020
"""

# I was able to make this program work with the following inputs:
# a = 1
# b = -1.5
# c = -1
# low = -100
# high = 100
# other combinations resulted in an infinite loop. been troubleshooting but can't find the bug.
# i will follow up with Kevin to figure this out. I feel like I'm so close. 

# variables
print('solving ax^2 + bx + c = 0: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
low = int(input('low bracket = '))
high = int(input('high bracket = '))
iterations = 0
guess = (high + low)/2.0
epsilon = a * 10**-10

# calculation and loop:
quadratic = a * guess * guess + b * guess + c
while quadratic != 0:
    print('low = ', low, 'high = ', high, 'ans = ', guess)
    iterations += 1
    if quadratic < 0:       # if f(guess) is less than 0, change 'low' to 'guess'
        low = guess
    else:
        high = guess        # otherwise, change 'high' to 'guess'
    guess = (high + low) / 2.0      # then change 'guess' to be halfway between 'low' and 'high'
    quadratic = a * guess * guess + b * guess + c       # solve for quadratic again and restart loop

# output

print('one root is: ', guess)
print('took', iterations, 'iterations')
