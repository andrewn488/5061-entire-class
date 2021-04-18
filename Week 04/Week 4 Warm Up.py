"""
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
Week 4 Practice
10/6/2020
"""
# CODE TRACING EXAMPLE
#dna = 'taaatcca'
#repeater, n, longest = 'a', 0, 0
#for base in dna:
#    if base == repeater[-1]:
#        repeater += base
#        n = 0
#    else:
#        n += 1
#        if n > longest:
#            longest = n
#print(repeater, longest)

# CODE TRACING PRACTICE
#a,b,c,k = 10,100,2,15
#result = ""
#for i in range(a, b, c):
#    if len(result) + len(str(i)) + 1 > k:
#        result += "..., "
#    result += str(i) + ", "
#result = result[:-2]  # take off ", " from end
#print(result)

# REVIEW QUESTION 1
#print('input five animal names')
#animal_1 = input('animal 1 name: ')
#animal_2 = input('animal 2 name: ')
#animal_3 = input('animal 3 name: ')
#animal_4 = input('animal 4 name: ')
#animal_5 = input('animal 5 name: ')

#if len(animal_1) > len(animal_2) and len(animal_3) and len(animal_4) and len(animal_5):
#    print(animal_1.upper())
#elif len(animal_2) > len(animal_1) and len(animal_3) and len(animal_4) and len(animal_5):
#    print(animal_2.upper())
#elif len(animal_3) > len(animal_2) and len(animal_1) and len(animal_4) and len(animal_5):
#    print(animal_3.upper())
#elif len(animal_4) > len(animal_2) and len(animal_3) and len(animal_1) and len(animal_5):
#    print(animal_4.upper())
#elif len(animal_5) > len(animal_2) and len(animal_3) and len(animal_4) and len(animal_1):
#    print(animal_5.upper())

# REVIEW QUESTION 2
#digit_count = 0
#char_count = 0
#type_something = input('Type something: ')
#for i in type_something:
#    if(i.isdigit()):
#        digit_count += 1
#    char_count += 1
#
#print(digit_count, 'digit characters')
#print(char_count, 'characters')

# REVIEW QUESTION 3

##char_count = 0
##type_something = str(input('Type something: '))
##for i in type_something:
##    if 'b' <= i <= 'f':
##        char_count += 1
##print(char_count, 'characters')

# REVIEW QUESTION 4
##import random
##n = random.uniform(-100, 100)
##print(n)


# REVIEW QUESTION 5
##from random import choice
##area_code = choice(['206', '253', '360', '564', '425'])
##print(area_code)

##x = 0
##y = 3
##greeks = 'αβγδεζηθικλμνξοπρστυφχψω'
##for char in greeks:
##    print(greeks[x:y])
##    x += 1
##    y += 1



##name = input('Enter Name: ')
##for i in name:
##    print(i.upper())

##string = input('Enter string: ')
##quantity = int(input('Enter quantity: '))
##
##for i in range(quantity):
##    print(string)
               
##x = 0
##y = 2
##japanese = 'いい子はみんな元気です'
##for i in japanese:
##    print((japanese[x:y]))
##    x += 1
##    y += 1
    
##import random
##n = 1000 * 1000
##low = -103
##high = 914
##even = 0
##middle = 0
##total = 0
##middle_low = low + (high - low) / 4
##middle_high = high + (high - low) / 4
##
##for i in range(n):
##    num = random.randint(low, high)
##    if num % 2 == 0:
##        even += 1
##    if middle_low <= num <= middle_high:
##        middle += 1
##    total += num
##print('Even: ', even / n * 100, '%')
##print('Middle: ', middle / n * 100, '%')
##print('Mean: ', total / n)

def foo():
    print('1')
    return True

if False and foo():
    print('2')

##import random
##n = random.randint(1,100)
##print(n)
# YES

##from random import *
##n = randint(1, 100)
##print(n)
# YES
    
##import random
##n = randint(1, 100)
##print(n)
# NO

##import random
##randint = random.randint
##n = randint(1, 100)
##print(n)
### YES
