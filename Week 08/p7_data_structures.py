"""P7: Data Structures
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
Date: 11/3/2020
"""

import numbers

# function 1
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

    count = 0
    for element in str_seq:
        if element.startswith(prefix):
            count += 1
    return count

# function 2
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

    new_list = []
    for element in sequence:
        if isinstance(element, numbers.Number) == True:
            new_list.append(element)

    return new_list

# function 3    
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

    total = 0
    seq = get_numbers(sequence)
    for element in seq:
        total += element

    return total


# function 4
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
    """
    # You must use the following dictionary:
    bp_map = {'a': 0, 'c': 1, 'g': 2, 't': 3}

    # YOUR CODE HERE


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

    # YOUR CODE HERE



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

    # YOUR CODE HERE



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

    # YOUR CODE HERE


def max_value(d):
    
