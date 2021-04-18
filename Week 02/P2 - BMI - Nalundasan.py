"""
P2 - BMI
Andrew Nalundasan
9/23/2020

Write a Python program that asks for a patient's height in feet and inches
and their weight in pounds and outputs their BMI. BMI is weight in kilograms
divided the square of the height in meters (BMI units are kg/m2).
Also output a message saying if the patient is obese (at least 30),
overweight (at least 25 but less than 30), ideal [15-25), or
underweight (<15).

Your program must use elif where applicable.
"""

# get input from user
print('Height in feet and inches: ')
height_ft = int(input("feet: "))     # height in feet
height_in = int(input("inches: "))   # height in inches
weight = int(input("Weight in pounds: "))    # weight in pounds

height_total_in = (height_ft * 12) + height_in  # total inches
height_metric = height_total_in * 0.0254    # convert height from in to m
weight_metric = weight * 0.453592   # convert weight from lb to kg
BMI = weight_metric / (height_metric ** 2) # calculate BMI using metric UOM

# calculate BMI result
print(f'weight: {weight_metric:.2f}kg')
print(f'height: {height_metric:.2f}m')

if BMI < 15:
    print(f'BMI: {BMI:.2f} (underweight)')
elif BMI < 25:
    print(f'BMI: {BMI:.2f} (ideal)')
elif BMI < 30:
    print(f'BMI: {BMI:.2f} (overweight)')
else:
    print(f'BMI: {BMI:.2f} (obese)')
    
