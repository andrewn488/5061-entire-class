# Teamwork 1: Bullet Exercise

#Author: Andrew Nalundasan

#For: 5061f20, Week 1, Bullet Range Exercise

import math
from math import sin, radians

# initialize what we know
v = 800     # speed (ft/s)
g = 32.2    # gravity of Earth (ft/s**2)

# get input from user
theta = float(input('Enter Angle: '))   # Angle (degree)

# calculate result
r = (v**2 * math.sin(2 * math.radians(theta)))/g

# output answer
print(f'The expected range of a bullet from a Colt .45 revolver is {r:.2f} feet')
