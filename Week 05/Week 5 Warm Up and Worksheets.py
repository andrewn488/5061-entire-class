"""
Week 5 warm up and worksheets - Functions
Andrew Nalundasan
10/13/2020
OMSBA 5061
"""

# Print out a table of the integers from 1 to 10 and for each
# row also print out the square and the cube of the number



##print('+--------+--------+--------+')
##print('|      i |    i^2  |   i^3  |')
##print('+--------+--------+--------+')
##for i in range(1, 11):
##    print('| %4d   | %4d   | %4d   |' % (i, i*i, i*i*i))
##    print('+--------+--------+--------+')

# Quadratic practice from video using FUNCTIONS
##import random
##a = 1.0
##b = 3.0
##c = -18.0
##epsilon = 1e-10
##
##def f(x):
##    """Evaluate polynomial at x."""
##    y = a * x ** 2 + b * x + c
##    return y
##
##def fp(x):
##    """Evaluates the derivative of the polynomial at x."""
##    yp = 2 * a * x + b
##    return yp
##
##guess = random.uniform(-100.0, + 100.0)
##while abs(f(guess)) > epsilon:
##    guess -= f(guess) / fp(guess)
##print('one root is', guess)

# Defining a Function
##def f(x):
##    y = 3 * x**2 - 2 * x + 3
##    return y
##
##x = -3.0
##
##while x <= 3.0:
##    print('| %6.2f | %6.2f |' % (x, f(x)))
##    x += 0.25
##    

s = 'claw foot tubbies'
##count = 0
##for c in s:
##    if 'a' <= c <= 'f':
##        count += 1
##print(count)

def countchars(s):
    """return the number of characters between a and f in a string"""
    count = 0
    for c in s:
        if 'a' <= c <= 'f':
            count += 1
    return count
countchars('claw foot tubbies')
