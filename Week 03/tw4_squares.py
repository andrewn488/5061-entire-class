"""
Week 3 Team Work Assignments
TW4_Odometer_Squares
9/30/2020
Chequala Fuller
Austin Bednar
Andrew Nalundasan
"""

# import math package
import math

# variables 
lownumber = int(input('low: '))
squareroot = math.sqrt(lownumber)
highnumber = int(input("high: "))


#reverse integers if low > high
if lownumber > highnumber:
    lownumber, highnumber = highnumber, lownumber

# range between low and high
for lownumber in range(lownumber, highnumber + 1):
    squareroot = math.sqrt(lownumber)
    squaredlownumber = int(squareroot) * int(squareroot)
    if lownumber == squaredlownumber:
        print(squaredlownumber)
    

