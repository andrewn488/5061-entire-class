"""
Week 3 Team Work Assignments
TW5 - Random Check - Random Counter
10/1/2020
Chequala Fuller
Austin Bednar
Andrew Nalundasan
"""

import random


count = 0

# step 1
count = 0
even = 0
odd = 0

# step 2
positive = 0
negative = 0
zero = 0

# step 3
occur_neg_1000 = 0
occur_0 = 0
occur_pos_1000 = 0

# challenge
current_odd_streak = 0
odd_streak_record = 0

while count < 100000:
    x = random.randint(-1000, 1000)
    # print(x)
    count += 1
    if (x % 2) != 0:
        odd += 1
    else:
        even += 1
    if (x < 0):
        negative += 1
    elif (x > 0):
        positive += 1
    elif (x == 0):
        zero += 1
    if x == -1000:
        occur_neg_1000 += 1
    elif x == 0:
        occur_0 += 1
    elif x == 1000:
        occur_pos_1000 +=1
        if x % 2 != 0:
            odd_streak_record += 1
        if current_odd_streak > odd_streak_record:
            current_odd_streak = odd_streak_record
        else: current_odd_streak = 0
print('There are {} even numbers'.format(even))
print('There are {} odd numbers'. format(odd))
print('The ratio between odd and even is', even/odd, 'ratio')
print('There are {} positive numbers'.format(positive))
print('There are {} negative numbers'.format(negative))
print('There are {} counts of zero'.format(zero))
print('The ratio between positive and negative is', positive/odd, 'ratio')
print('There are {} occurrences of -1000'.format(occur_neg_1000))
print('There are {} occurrences of 0'.format(occur_0))
print('There are {} occurrences of 1000'.format(occur_pos_1000))
print('Longest odd streak was: ', current_odd_streak)
print('Longest odd streak was: ', odd_streak_record)
