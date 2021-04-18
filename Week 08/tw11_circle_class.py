""" TW11: Circle Class
Team: Tam Tamura, Andrew Nalundasan
For: OMSBA 2061, Seattle University
Date: 11/6/2020
"""

from math import pi
from turtle import Turtle

class Circle(object):
    def __init__(self, radius, x = 0, y = 0, color = 'white'): # set default to white
        self.radius = radius
        self.location = (x, y)
        self.turtle = Turtle()
        self.color = color
        

    def area(self):         # method for area
        return pi * (self.radius**2)

    def perimeter(self):    # method for perimeter
        return 2 * pi * self.radius

    def x_coord(self):      # method for x coord
        return self.location[0]

    def y_coord(self):      # method for y coord
        return self.location[1]

    def center(self):       # method for x and y coords
        return (self.x_coord, self.y_coord)

    def render(self):       # method for turtle plotting
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.setposition(self.location)
        self.turtle.color(self.color)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()


