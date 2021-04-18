""" P7: Data Structures
Author: Andrew Nalundasan
For: OMSBA 2061, Seattle University
Date: 11/8/2020
"""

import numbers

def count_common_prefix(str_seq, prefix):
    """ Take any sequence of strings, str_seq, and return the count of
        element strings that start with the given prefix.

        >>> count_common_prefix(('ab', 'ac', 'ad'), 'a')
        3
        >>> count_common_prefix(['able', 'baker', 'adam', 'ability'], 'ab')
        2
        >>> count_common_prefix([], 'a')
        0
        >>> count_common_prefix(['a', 'a', 'ab'], 'a')
        3
        >>> count_common_prefix(['a', 'a', 'ab'], '')
        3
    """
    # Hint: use string method str.startswith

    count = 0       # initialize to 0
    for elem in str_seq:    # iterate over all elements in str_seq
        if elem.startswith(prefix):
            count += 1      # increment count if elem starts with the prefix
    return count


def get_numbers(sequence):
    """ Take any sequence and return a list of all elements that are
        numbers.

        >>> get_numbers(range(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> get_numbers([1, 2.5, '3'])
        [1, 2.5]
        >>> get_numbers('abc123.4xyz')
        []
        >>> get_numbers((1, 2.5, complex(3, 4), '5'))
        [1, 2.5, (3+4j)]
        
    """
    # Hint: use isinstance(element, numbers.Number)

    new_list = []           # create empty list
    for element in sequence:
        if isinstance(element, numbers.Number) == True:     # check if all elements are the same, numbers in this case
            new_list.append(element)        # append the list
    return new_list


def sum_numbers(sequence):
    """ Take any sequence and return the sum of all elements that are
        numbers. Non-numbers are ignored.

        >>> sum_numbers(range(10))
        45
        >>> sum_numbers([1, 2.5, '3'])
        3.5
        >>> sum_numbers('abc123.4xyz')
        0
        >>> sum_numbers((1, 2.5, complex(3, 4), '5'))
        (6.5+4j)
        
    """
    # Hint: use built-in function sum and your own get_numbers function

    total = 0       # initialize at 0
    seq = get_numbers(sequence)  # call get_numbers function to use on provided sequence
    for elem in seq:             # iterate over all elements in seq
        total += elem            # increment elem to the total
    return total


def dna_digit(bp):
    """ Take a character (a string of length one) and return a
        0 for 'a', 1 for 'c', 2 for 'g', and 3 for 't'. For any
        other string, raise a ValueError. Capital or lowercase letters
        are acceptable.

        >>> dna_digit('a')
        0
        >>> dna_digit('C')
        1
        >>> dna_digit('g')
        2
        >>> dna_digit('t')
        3
        >>> dna_digit('abc')
        Traceback (most recent call last):
            ...
        ValueError: only 'a', 'c', 'g', or 't' accepted
        >>> dna_digit("")
        Traceback (most recent call last):
            ...
        ValueError: only 'a', 'c', 'g', or 't' accepted
    """
    # You must use the following dictionary:
    bp_map = {'a': 0, 'c': 1, 'g': 2, 't': 3}
    lower_bp = bp.lower()       # set all tests to lowercase to be evaluated same as upper case

    if lower_bp in bp_map:      # use dict in lowercase to make evaluation
        return bp_map[lower_bp]
    else:
        raise ValueError("only 'a', 'c', 'g', or 't' accepted")


def bp_from_digit(digit):
    """ Inverse of dna_digit.

        >>> bp_from_digit(3)
        't'
        >>> bp_from_digit(7)
        Traceback (most recent call last):
            ...
        ValueError: only 0, 1, 2, or 3 accepted
    """
    # You must use the following dictionary:
    bp_map = {0: 'a', 1: 'c', 2: 'g', 3: 't'}

    if digit in bp_map:
        return bp_map[digit]    # returns only values with corresponding keys
    else:
        raise ValueError("only 0, 1, 2, or 3 accepted")


def dna_number(bp_seq):
    """ Take a dna string, bp_seq, (a string of a's, c's, g's, and t's)
        and interpret that as a base-4 number using dna_digit for each
        basepair. A ValueErorr is raised if there are any characters besides
        those accepted by dna_digit.

        >>> dna_number('')
        0
        >>> dna_number('aaa')
        0
        >>> dna_number('t')
        3
        >>> dna_number('ca')
        4
        >>> dna_number('CAA')
        16
        >>> dna_number('cgt')
        27
        >>> dna_number('cggaattAGGTtttacgtactggatcaat')
        117360495799280451
        >>> dna_number('whatever')
        Traceback (most recent call last):
            ...
        ValueError: only 'a', 'c', 'g', or 't' accepted
        >>> dna_number(['c', 'g', 't'])  # should work for any sequence type
        27
    """
    # Hint: use dna_digit

    if bp_seq == '':    # return 0 if empty sequence
        return 0
    seq = ''
    for digit in bp_seq:
        seq += str(dna_digit(digit))    # concatenate seq with strings of the digit
        
    return int(seq, base = 4)


def chunks(sequence, chunk_size):
    """ Take any sequence and a chunk size, and return a list of the chunks
        from the given sequence.
        
        >>> chunks('cgtcgtcgtaaa', 3)
        [['c', 'g', 't'], ['c', 'g', 't'], ['c', 'g', 't'], ['a', 'a', 'a']]
        >>> chunks('cgtcgtcgtaaa', 5)
        [['c', 'g', 't', 'c', 'g'], ['t', 'c', 'g', 't', 'a'], ['a', 'a']]
        >>> chunks(range(7), 2)
        [[0, 1], [2, 3], [4, 5], [6]]
        >>> chunks(((1,2), ['a','b','c'], 'xyz'), 1)
        [[(1, 2)], [['a', 'b', 'c']], ['xyz']]
    """

    my_list = []                                        # empty list
    for elem in range(0, len(sequence), chunk_size):    # start at position 0 for len of sequence with stride for chunk_size
        my_list.append(list(sequence[elem:elem + chunk_size]))  # append the list
    return my_list


def substring_list(s, k):
    """ Takes a string, s, and and length, k, and returns a list of all
        the substrings in s of length k (including overlap).

        >>> substring_list('abcdefg', 2)
        ['ab', 'bc', 'cd', 'de', 'ef', 'fg']
    """

    my_list = []                            # create empty list
    for elem in range(len(s) - k + 1):      # use + 1 to capture the overlap
        my_list.append(s[elem:elem + k])    # append the list with substrings
    return my_list


def max_value(d):
    """ Takes a dictionary d and returns the maximum element value and its
        corresponding key. Raises a TypeError if any of the values are not
        comparable to each other.

        >>> max_value({'a': 12, 3: 45})
        (3, 45)
        >>> max_value({}) is None
        True
        >>> max_value({33: 34, -1: 600, 'xyz': 2000.4})
        ('xyz', 2000.4)
        >>> max_value({1: 'abc', 2: 'xyz', 3: 'ghijkl'})
        (2, 'xyz')
        >>> max_value({1:'a', 2:3}) # doctest:+ELLIPSIS
        Traceback (most recent call last):
            ...
        TypeError:...
    """
    # Hint: d.values() is a sequence of all the values in dictionary d
    #       try using this along with built-in function max

    if d == {}:                 # if empty, return None
        return None
    max_key = ''                # initialize max_key as ''
    max_val = max(d.values())   # set max_val to the max of all values in d
    for key in d.keys():        # iterate over all keys in d
        if d[key] >= max_val:
            max_val = d[key]    # set d[key] to max_val if it's the highest that's been iterated over
            max_key = key       # assign max_key when max_val is assigned 
    return (max_key, max_val)



def dna_most_common(bp_seq, k):
    """ Takes a sequence of dna base pairs, bp_seq, and a substring size, k,
        and returns the most common substring of length k in bp_seq and also
        the count.

        >>> dna_most_common('cccgggaaatatctgtttt', 1)
        ('t', 7)
        >>> dna_most_common('cgagttatgagacgacgacga', 3)
        ('cga', 4)
        >>> dna_most_common('ttttttt', 4)
        ('tttt', 4)
    """
    # Implementation: create a dictionary keyed by substring (gotten with
    # substring_list function). The values of the dictionary are the number
    # of times we've seen that substring.
    # This is MUCH faster than our approach earlier in the quarter.

    substring_count = {}
    substrings = substring_list(bp_seq, k)

    for elem in substrings:     # iterate over each element in substrings
        if elem in substring_count:
            substring_count[elem] += 1      # increment substring_count if elem is in substring_count
        else:
            substring_count[elem] = 1       # start the count of key and value as 1
    return max_value(substring_count)       # return most common substring and count
