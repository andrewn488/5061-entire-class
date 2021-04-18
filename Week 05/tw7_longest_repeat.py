"""TW7: Longest Repeat
Team: Tam Tamura, Austin Bednar, Andrew Nalundasan
For: OMSBA 5061, Seattle University
Date: 10/16/2020
"""

def longestRepeat(substring, string):
    counter = 0
    count = 0
    maxnum = 0
    mastervalue = substring
    previousvalue = substring
    for substring in string:
        if substring == mastervalue and previousvalue == substring:
            counter += 1
        else: counter = 0
        if counter > maxnum:
            maxnum = counter
    previousvalue == substring
    return maxnum
string = "trtrzzzooozz"
substring = "o"
print(longestRepeat(substring,string))
