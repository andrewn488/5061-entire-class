"""
P2 - Sum
Andrew Nalundasan
9/23/2020
Write a Python program that reads in numbers from the user until they type
STOP, then print out the count, the sum, and the mean, i.e., sum/count.
Make sure it works even if they type STOP right away. Don't worry about
handling the exception (i.e., the program "crashing") if they type in
something that is not a number or STOP.
"""

# inputs
user_data = input('Enter a number to sum(type STOP to finish): ')

# variables
total_sum = 0   # sum starts at 0
total_count = 0     # count starts at 0

# loop
while user_data != 'STOP':  # loop continues to run as long as != 'STOP'
    number = int(user_data)     # convert user input to integer
    total_sum += number     # starting at 0, keep adding to get sum
    total_count += 1    # increment total count each iteration
    user_data = input('Enter a number to sum(type STOP to finish): ')   # continue the loop

# Output
print('Count: {}'.format(total_count))
print('Sum: {:.1f}'.format(total_sum))

# Output for Mean if 'STOP' is first entry
if total_count == 0:
    print('Mean: 0.0')
else:
    print('Mean: {:.1f}'.format(total_sum / total_count))






                 
