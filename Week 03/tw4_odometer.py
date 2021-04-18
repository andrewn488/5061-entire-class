"""
Week 3 Team Work Assignments
TW4_Odometer
9/30/2020
Chequala Fuller
Austin Bednar
Andrew Nalundasan
"""

# user inputs and variables
# 987.5 = 9 hundreds, 8 tens, 7 ones, 5 tenths

tenths = 0
ones = 0
tens = 0
hundreds = 0
            
# 4-tiered nested loop

for hundreds in range(10):
    for tens in range(10):
        for ones in range(10):
            for tenths in range(10):
                print(hundreds, tens, ones, '.', tenths)




