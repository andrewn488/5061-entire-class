""" TW10: Words by Prefix
Team: Tam Tamura, Andrew Nalundasan
For: OMSBA 2061, Seattle University
Date: 11/3/2020
"""

def wordByPrefix(prefix_length, word):
    my_dict = {}
    for key in word:
        for letter in word:
            prefix_key = letter[:prefix_length]
            letter = word[:prefix_length]
            return prefix_key
    return letter


question_2 = ['able', 'ability', 'apple', 'tryst', 'trial', 'tremendous', 'tree']
my_list = []
for elem in question_2:
    prefix = elem[:2]
    my_list.append(prefix)
print(my_list)
    


def question_3(prefix_length, word):
    my_list = []
    for key in word:
        prefix = key[:prefix_length]
        my_list.append(prefix)
    return my_list


def wordByPrefix(prefix_length, word):
    my_list = []
    #count = 0
    for key in word:
        prefix = key[:prefix_length]
        my_list.append(prefix)
        count = {}
        for letter in my_list:
            if letter.isalpha():
                if letter not in count:
                    count[letter] = 0
                count[letter] += 1
    return count


def wordByPrefix(prefix_length, word):
    my_list = []
    #count = 0
    for key in word:
        prefix = key[:prefix_length]
        my_list.append(prefix)
        count = {}
        for letter in my_list:
            if letter.isalpha():
                if letter not in count:
                    letter[count] = []
                    count.update(letter)
    return count
