"""PEC1: Decimal to Binary
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
"""
   
print('When you enter a non negative integer a string in binary representation will be shown')
n = int(input('Enter a non- negative integer: '))
if n < 0:
    print('You must enter a non- negative integer: ')
    print('Please try again')
    n = int(input('Enter a non- negative integer: '))
​
def decimalToBinary (n):
    """ Returns a string with the binary number representation
    for any non- negative ineger
    """
    if n == 0:
        n = '0'
    while n > 0:
        if n % 2 != 0:
            n = (([n / 2]) + '1')
        elif n % 2 == 0:
             n = (([n / 2]) + '0')
    return n
print ('{:b}'.format (n))
