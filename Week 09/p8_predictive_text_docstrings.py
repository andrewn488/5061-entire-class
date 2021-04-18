"""P8: Predictive Text
For: OMSBA 5061, Seattle University
Author: Andrew Nalundasan
Date: 11/15/2020
Instructor-provided docstrings for selected methods

Had trouble with 'best' and 'possible' methods. Difficulty debugging.
Got started on '_perform_chaching'.
Couldn't start 'possible_prefixes'. 
"""
# FIXME Change the following line to reflect the location of the downloaded file
WORD_LIST_FILE = '.English_words_by_usage_rank.txt'
PREFIX_SIZE = 3     # needs to be > 0

class PText(object):
    """Predictive Text
    >>> p = PText()
    >>> p.add('742')
    >>> p.possible()
    ['pick', 'shake', 'rich', 'share', 'shadow', 'sick', 'sharp', 'shall', 'phase', 'shape',
    'rice', 'shade', 'piano', 'shame', 'pickup', 'picture', 'sharply', 'shared', 'shallow',
    'sibling', 'shark', 'rib', 'shareholder', 'ribbon']
    >>> p.best()
    'pick'
    >>> p.add('9')
    >>> p.possible()
    []
    >>> p.backspace()
    >>> p.add('8')
    >>> p.possible()
    ['picture']
    >>> p.best()
    'picture'
    >>> p.backspace()
    >>> p.add('7')
    >>> p.possible()
    ['share', 'sharp', 'phase', 'shape', 'sharply', 'shared', 'shark', 'shareholder']
    """

    key_map = {'1': "'-", '2': 'abc', '3': 'def',
               '4': 'ghi', '5': 'jkl', '6': 'mno',
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    words_by_prefix = None
    rank_by_words = None

    def __init__(self):
        """Start a new word in the flip phone texting app."""
        self.key_presses = ''

    def add(self, key_presses):
        """Append a new key press (or a sequence of them) onto current word.
        keyPress -- '2', '3', ..., '9' from telephone keypad
        """
        for k in key_presses:       # for every sequence or str provided, add a key press
            self.key_presses = self.key_presses + k

    def backspace(self):
        """Remove last key press from current word (backspace)."""
        if len (self.key_presses) > 0:      # only update if a string of digits actually exists
            self.key_presses = self.key_presses[:-1]    # backspace from the end of the string. [:-1] is end of string

    def best(self):
        """Return the most likely English word for the current key sequence.
        Assumes at least 3 keystrokes have been entered (raises ValueError
        otherwise).
        """
        # ensure min number of key strokes has been met
        if len(self.key_presses) < PREFIX_SIZE:
            raise ValueError("You must enter a minimum of %d keystrokes." % PREFIX_SIZE)

        for word in self.possible():        # this should be in order
            return word         # return first valid word since it will be at top of list
        return ''               # else: return empty string

    def possible(self):
        """Returns a list of possible words given the current key sequence.
        Assumes at least 3 keystrokes have been entered (raises ValueError
        otherwise). Returned in rank order.
        """
        self._perform_caching()         # can't get this method to work. incomplete code
        
        # ensure min number of key strokes has been met
        if len(self.key_presses) < PREFIX_SIZE:
            raise ValueError("You must enter a minimum of %d keystrokes." % PREFIX_SIZE)
        
        next_word = ''
        last_rank = 0
        # generate word at end of while loop
        while next_word is not None:
            next_word = None    # leave next_word as null until something is keyed in
            current_rank = -1   # clear out current rank
            for prefix in self.possible_prefixes():         # check all possible words
                if prefix not in self.words_by_prefix:      # skip prefixes not in .txt file
                    continue
                for word in self.words_by_prefix[prefix]:   # check all possible words using this prefix
                    if not self.matches(word):              # skip if word doesn't match up
                        continue
                    rank = self.rank_by_words[word]         # compare current rank vs previous rank
                    if rank <= last_rank:                   # skip word if we had this rank already
                        continue
                    if next_word is None or rank < self.rank_by_words[next_word]:   # save the rank & word if next highest rank
                        next_word = word
                        current_rank = rank

            if next_word is not None:
                yield next_word                             # yield to return a value from a class
                last_rank = current_rank                    # continue loop where we left off (from last_rank)
            

    def _perform_caching(self):
        """Read word list into data structures that we will use:

        words_by_prefix -- a dictionary that contains a list of words in rank
                         order for each 3-letter prefix encountered in the
                         word list

        rank_by_words -- a dictionary that maps each word to its rank

        If these are already filled in (not None), then return immediately.

        Reads the word list file, WORD_LIST_FILE, which has all possible
        English words (that we will consider) listed in rank order.
        """
        if PText.words_by_prefix is not None:               # code provided from prof
            return

        words_file = open(WORD_LIST_FILE, 'r')      # open file in read mode

        # create empty dictionaires
        words_by_prefix = {}
        rank_by_words = {}
        rank = 0        # first line of the file
        ### for line in words_file:         
            ### having trouble working out logic in this loop. stopping here.
        

    def possible_prefixes(self, level = 0, prefix = ''):
        """Generate a list of all 3-character prefixes that can be
        generated from the beginning key presses.
        >>> pt = PText()
        >>> pt.add('234')
        >>> [prefix for prefix in pt.possible_prefixes()]
        ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi',
        'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei',
        'cfg', 'cfh', 'cfi']
        """
        # ensure min number of key strokes has been met
        if len(self.key_presses) < PREFIX_SIZE:
            raise ValueError("You must enter a minimum of %d keystrokes." % PREFIX_SIZE)

        ### not sure where to start on this method...

    def matches(self, word):
        """Checks if all the current keypresses exactly match the letters
        of word.
        >>> pt = PText()
        >>> pt.add('222')
        >>> pt.matches('backlog')  # 2->b, 2->a, 2->c so yes
        True
        >>> pt.matches('a')  # too short, cannot match 222
        False
        """

        if len(word) < len(self.key_presses):            # word won't match if len is lesser than amount of key presses
               return False

        for i in range(len(self.key_presses)):
            char_from_word = word[i]
            key_press = self.key_presses[i]
            if char_from_word not in PText.key_map[key_press]:          # if get a typo from user
                return False            # exit loop and return False

        return True                     # otherwise, exit loop and return True
    

