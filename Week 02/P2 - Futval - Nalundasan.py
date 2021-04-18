"""
P2 - Futval
Andrew Nalundasan
9/23/2020
Write a Python program that reads in investment amount, annual interest rate,
and number of years, and displays the future investment value using the
following formula (called monthly compounding):
For example, if you enter amount 1000, annual interest rate 3.25%, and number
of years 1, the future investment value is 1032.99
"""

# what we know

investment = int(input('Enter investment amount: '))    # get investment amount
annual_interest_rate = float(input('Enter annual interest rate: '))   # get annual interest rate
annual_percentage = annual_interest_rate / 100  # convert number to percentage
years = int(input('Enter number of years: ')) 
monthly_interest_rate = annual_percentage / 12  # convert annual % to monthly %
number_months = years * 12  # convert years to months

# calculate
future_value = investment * (1 + monthly_interest_rate) ** number_months

# output
print(f'Accumulated value is ${future_value:.2f}')
