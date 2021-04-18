"""Week 09 exercises
What: Warm up, worksheets, practice, worksheet 16
Author: Andrew Nalundasan
Date: 11/6/2020
"""

import math
from math import pi

my_seq = []
stragglers = []
def transpose(seq):
    for elem in seq:
        my_seq.append(elem[:-1])
        stragglers.append(elem[-1])
    return (my_seq, stragglers)


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

c = Circle(10.0)


# worksheet 16

##class MyClass(object):
##    foo = initial_value
##    bar = something_else
##
##print(MyClass.foo)  # reference to the foo class variable of MyClass


class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __repr__(self):
        return "Rectangle(%f, %f)" % (self.height, self.width)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height * 2) + (self.width * 2)
    

