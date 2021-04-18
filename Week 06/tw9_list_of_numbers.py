"""TW9: List of Numbers
Team: Bharti Lalwani, Austin Bednar, Andrew Nalundasan
For: OMSBA 5061, Seattle University
Date: 10/20/2020
"""


def inputList3(f, prompt = 'Enter a series of integers divisible by 3:'):
    result = []     # create empty list
    num = input(prompt)     # read the input
    while num != 'STOP':
        x = int(num)    # convert input to integer
        if f(x) == TRUE:    # passes the input to the function and checks if it is true;
            result.append(x)    # if true, then add to result list
        num = input('Next: ')   # get the next input
    return result

