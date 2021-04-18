""" TW12: Escape!
Team: Arunima Roy, Vishaal Diwan, Andrew Nalundasan
For: OMSBA 2061, Seattle University
Date: 11/13/2020
"""

# import necessary packages
import math
import random
from turtle import Turtle

class Escape:
    """ Class to simulate a person randomly walking from the center 
        until they get to a certain distance, r, from the origin.
    """
    def __init__(self, radius):
        self.radius = radius
        self.x = 0
        self.y = 0
        self.turtle = Turtle()  # instance reference to turtle

    def fence(self):
        """ Renders the "fence" as a circle with radius = self.radius without distrupting the current
            save x,y position of the escapee.
        """
        # clear canvas
        self.turtle.clear() 

        # reset drawing pos
        self.turtle.penup()
        self.turtle.setposition(0, -self.radius)
        self.turtle.pendown()

        # draw a circle of given radius
        self.turtle.color('red', 'white')
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()
        self.turtle.color('black', 'white')

        # revert current pos back to current walking location
        self.turtle.penup()
        self.turtle.setposition(self.x, self.y)
        self.turtle.pendown()

    def capture(self):
        """ Moves the escapee back the center of the circle without drawing this move.
        """
        # capture to origin
        self.x = 0
        self.y = 0
        # reset drawing pos to current position (origin)
        self.turtle.penup()
        self.turtle.setposition(self.x, self.y)
        self.turtle.pendown()

    def escape(self):
        """ Simulates escaping from the center of the fenced area.
        """
        # if the line from the origin to our current position is >= self.radius, then we want to finish
        # we know this because radius^2 = x^2 + y^2 for points on the circle of given radius
        # so r = sqrt(x**2 + y**2), thus if our own x,y positions are ON or Beyond the circle's radius
        # then that equation will give us an r which is >= self.radius, at which point we know to terminate
        while math.sqrt((self.x**2) + (self.y**2)) < self.radius:
            degrees_to_turn = random.randint(0, 360) # choose random walking degrees from 0 to 360
            self.turtle.right(degrees_to_turn) # turn right with random degrees, as specified
            self.turtle.forward(30) # move forward 30 meters (1 turtle unit = 1 meter)
            new_pos = self.turtle.position() # get the new position of the escapee
            # set our saved x,y to the new position
            self.x = new_pos[0]
            self.y = new_pos[1]
