"""
Newton-Raphson model for Square Root
Practice from Guttag textbook
10/2/2020 - Gabby's birthday!
Practice for assignment P3: Quadratic
"""

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0

# variables
#epsilon = 0.01
#k = 24.0
#iteration = 0

# calculation
#guess = k/2.0

# loop
#while abs(guess * guess - k) >= epsilon:
#    guess = guess - (((guess**2) - k)/(2 * guess))
#    iteration += 1

# output
#print('Square root of', k, 'is about', guess)
#print('took', iteration, 'iterations')


"""
Guidance from assignment:
"""
# variables: 
a = 1.0
b = -1.5
c = -1.0
iterations = 0
epsilon = a * 10**-10
f_guess = 3.0

# calculate and loop:

guess = a * f_guess * f_guess + b * f_guess + c
while guess >= epsilon:
    guess = a * f_guess * f_guess + b * f_guess + c
    f_guess = f_guess - (a * f_guess * f_guess + b * f_guess + c) / (2 * a * f_guess + b)
    iterations += 1

# output:
print('one root is: ', f_guess)
print('took', iterations, 'iterations')

"""
Guidance on Bisection
"""

x = 25
epsilon = 0.01
num_guesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ', low, 'high = ', high, 'ans = ', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print('numGuesses = ', num_guesses)
print(ans, 'is close to square root of', x)

