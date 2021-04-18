"""
Week 1 5-Minute Warmup

Write a program that gets a number from the user and prints out 3x that number
on the shell console
"""

#x = int(input('Is my number 3x the input? '))

#print(x * 3)



height = float(input('What is your height in inches? '))
if height < 60.0:
    print('very short')
else:
    if height < 68.0:
        print('short')
    else:
        if height < 72.0:
            print('average')
        else:
            print('tall')


height = float(input('What is your height in inches? '))
if height < 60.0:
    print('very short')
elif:
    height < 68.0:
        print('short')
elif:
    height < 72.0:
        print('average')
else:
    print('tall')
