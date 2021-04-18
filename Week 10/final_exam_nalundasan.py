"""
Final Exam - Counter
Author: Andrew Nalundasan
For: OMSBA 5061
Date: 11/24/2020
"""

class Counter(object):
    """Keeps track of a dictionary of words and the frequency that the words
    are encountered in a file. Keeps track of how many unique words as well
    as the total number of words encountered.
    """

    def __init__(self):
        """Initializes all necessary attributes"""

        # no attributes needed. doctest has "c = Counter()" so no positional
        # arguments needed.
        
        
        
    def read_file(self, f):
        """Takes in a filename and reads, word by word"""
        self.f = f
        filename = open(f, 'r')    # open file in read mode.
        contents = filename.read()    # read file line by line
        filename.close()        # close the file
    
    def add_word(self, add_word):
        """Takes in a word. If the word does not exist, adds word to
        dictionary, sets the word count to 1, and updates the unique word
        count. If the word does exist, increments the count of the given
        word in the dictionary. Update the total word count, regardless of
        whether the word does or does not exist. Make sure the word is cleaned
        before adding to the dictionary. Note that this function is not
        called in the test below; determine where it should be called.
        """
        self.add_word = add_word

        tot_count = 0
        count = 0    # set word count to 0
        for add_word in contents:     # read the contents
            if add_word not in contents:
                contents += add_word
                count = 1
                tot_count += 1

        contents.clean_word()
        read_file.contents += add_word        
        
    def remove_word(self, remove_word):
        """Takes in a word. The remove method should completely remove the
        entry from the dictionary. Update the unique and total word counts
        if necessary. Raises KeyError if word is not in dictionary.
        """

        self.remove_word = remove_word    # word to remove

        for word in contents:    # read the contents
            if word == self.remove_word:
                word = ''    # remove the word
            if word not in read_file.filename:
                raise KeyError('word is not in the dictionary') 

    def get_count(self, spec_word):
        """Returns the count of the specified (passed in) word. If the word
        has not been encountered before, return 0.
        """
        self.spec_word = spec_word

        self.count = 0
        for word in contents:     # iterate thru contents
            if word == spec_word:    # if word == specified word, increment
                self.count += 1
            else:
                return 0.0    # else return 0

        return count

    def clean_word(self, clean):
        """Takes in a word and converts it to lower case. Removes special
        characters that are not hyphen or apostrphe. Returns the clean result.
        Note that this function is not called in the test below; determine
        where it should be called.
        """
        self.clean = clean

        for word in contents:
            clean = word.lower()

    def get_sorted(self, d):
        """Returns sorted dictionary, but makes no changes to the original
        dictionary.
        """

        d = read_file.contents()    # read the dictionary
        d.sort()            # sort the dictionary
        return d        # return sorted dictionary

        
    
