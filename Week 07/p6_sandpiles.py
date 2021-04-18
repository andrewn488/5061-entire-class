"""P6: Sandpiles (Extra Credit)
Author: Andrew Nalundasan
Collaborator: Arunima Roy
For: OMSBA 5061, Seattle University
Date: 11/1/2020
"""

# function 1
def printPile(a):
    """print the sanpile, a, nicely"""
    for elem in a:
        print(elem)
    return

# function 2
def isStablePile(a):
    """Returns true is a is stable, false otherwise"""
    false_count = 0
    for row in a:
        for column in row:
            if column > 3:
                false_count += 1
        if false_count > 0:
            return False
        else:
            return True

# function 3

def topplePile(a):
    """ when stable pile, return a. when unstable, topple cells >= 4 until stable.
    call isStablePile to verify afterwards"""
    top_left = a[0][0]      # assign variable to each cell of pile
    top_mid = a[0][1]
    top_right = a[0][2]
    mid_left = a[1][0]
    mid_mid = a[1][1]
    mid_right = a[1][2]
    bot_left = a[2][0]
    bot_mid = a[2][1]
    bot_right = a[2][2]
    for row in a:           # if cell >= 4, then topple to neighbor cells
        for column in row:
            if top_left >= 4:
                top_left = 0
                top_mid += 1
                mid_left += 1
            elif top_mid >= 4:
                top_mid = 0
                top_left += 1
                top_right += 1
                mid_mid += 1
            elif top_right >= 4:
                top_right = 0
                top_mid += 1
                mid_right += 1
            elif mid_left >= 4:
                mid_left = 0
                top_left += 1
                mid_mid += 1
                bot_left += 1
            elif mid_mid >= 4:
                mid_mid = 0
                mid_left += 1
                top_mid += 1
                mid_right += 1
                bot_mid += 1
            elif mid_right >= 4:
                mid_right = 0
                top_right += 1
                mid_mid += 1
                bot_right += 1
            elif bot_left >= 4:
                bot_left = 0
                mid_left += 1
                bot_mid += 1
            elif bot_mid >= 4:
                bot_mid = 0
                mid_mid += 1
                bot_left += 1
                bot_right += 1
            elif bot_right >= 4:
                bot_right = 0
                mid_right += 1
                bot_mid += 1
            else:                   # if a is stable, return a
                return a
    isStablePile(a)                 # call isStablePile after toppling to validate stability
# function 4

def addPiles(a, b):
    """returns the resulting sandpile of adding sandpile a to sandpile b
    and topple afterwards"""
    top_left = a[0][0]      # assign variable to each cell of pile
    top_mid = a[0][1]
    top_right = a[0][2]
    mid_left = a[1][0]
    mid_mid = a[1][1]
    mid_right = a[1][2]
    bot_left = a[2][0]
    bot_mid = a[2][1]
    bot_right = a[2][2]
    for row in a:
        for column in row:          # add each cell in a to corresponding cell in b
            top_left = a[0][0] + b[0][0]
            top_mid = a[0][1] + b[0][1]
            top_right = a[0][2] + b[0][2]
            mid_left = a[1][0] + b[1][0]
            mid_mid = a[1][1] + b[1][1]
            mid_right = a[1][2] + b[1][2]
            bot_left = a[2][0] + b[2][0]
            bot_mid = a[2][1] + b[2][1]
            bot_right = a[2][2] + b[2][2]
    return a
    toppliePile(a)          # topple pile a after adding pile b.
    isStablePile(a)         # verify if pile a is stable after calculations


# function 5, 6, 7
def zeroPile():
    """return zero sandpile for the group. no parameters given for arguments."""

def isInGroup(a):
    """determines if sandpile a is in group from Dr. Garcia-Puente's group, S"""
    if a + 0 = a:
        a = 'a is in s'
    else:
        a = 'a is not in s'
        
def countGroup():
    """count number of sandpiles in S. no parameters given for argument"""
    
## ran out of time. submitting what I have for partial credit. will definitely
## seek solution for this one. i'm interested to see how this is properly done.

    
