"""
TW2: Odd Numbers

Sohrab Rajabi
Mohammed Elhaj
Andrew Nalundasan

From three integers, x, y, and z pick the highest one that is odd (or output
a message that they are all even.
"""
# get the input from user
x = int(input('Enter x number: '))
y = int(input('Enter y number: '))
z = int(input('Enter z number: '))

# calculate the result
if(x % 2 == 0 and y % 2 == 0 and z % 2 == 0):
    print('all numbers are EVEN numbers')
elif(x % 2 != 0 and y % 2 == 0 and z % 2 == 0):
    print('only x is odd')
    print('The highest odd was x', x)
elif(x % 2 == 0 and y % 2 != 0 and z % 2 == 0):
    print('only y is odd')
    print('The highest odd was y', y)
elif(x % 2 == 0 and y % 2 == 0 and z % 2 != 0):
    print('only z is odd')
    print('The highest odd was z', z)
elif(x % 2 != 0 and y % 2 != 0 and z % 2 == 0):
    print('x and y are odd')
    maximum = x     # define maximum variable
    if y > x:
        maximum = y
        print(f'The highest odd was y: {y}')
    else:
        print(f'The highest odd was x: {x}')
elif(x % 2 != 0 and y % 2 == 0 and z % 2 != 0):
    print('x and z are odd')
    maximum = x
    if z > x:
        maximum = z
        print(f'The highest odd was z: {z}')
    else:
        print(f'The highest odd was x: {x}')
elif(x % 2 == 0 and y % 2 != 0 and z % 2 != 0):
    print('z and y are odd')
    maximum = y
    if z > y:
        maximum = z
        print(f'The highest odd was z: {z}')
    else:
        print(f'The highest odd was y: {y}')
elif(x % 2 != 0 and y % 2 != 0 and z % 2 != 0):
    maximum = x
    if y > maximum :
        maximum = y
    print(f'The highest odd was y', y)
elif z > maximum :
    maximum = z
    print(f'The highest odd was z', z)
else:
    print(f'The highest odd was x', x)
    


