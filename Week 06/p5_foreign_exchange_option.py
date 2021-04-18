"""P5: Foreign Exchange Option
Author: Andrew Nalundasan
Collaborator: Arunima Roy
For: OMSBA 5061, Seattle University
Date: 10/25/2020
"""

# import necessary libraries
import scipy      # statistics library
from scipy.stats import norm  # normal distribution statistics library
import math       
from datetime import date     # for years_apart function
​
# discount function
def discount(rate, term):
    """Calculate the discount factor for given simple interest rate and term.
    present_value = future_value * discount(rate, term)
    >>> discount(0.123, 0.0)
    1.0
    >>> discount(0.03, 2.1)
    0.9389434736891332
    """
    discount = math.e**(-rate * term)
    return discount
​
​# years_apart function
def years_apart(date1, date2):
      """Returns the fractional difference in years between the given dates.
    Assumes a 365-day year for the fractional part.
    >>> years_apart(date(1959, 5, 3), date(1960, 5, 3))
    1.0
    >>> years_apart(date(2004, 1, 1), date(2005, 1, 2)) # 365 days even if a leap year
    1.0027397260273974
    >>> years_apart(date(1959, 5, 1), date(2019, 6, 2))
    60.087671232876716
    >>> years_apart(date(2019, 7, 1), date(2019, 4, 1)) # reversed is ok
    0.2493150684931507
    """
    # ensure that date 1 is before date 2
    if(date2 < date1):
        date1, date2 = date2, date1
    cur_date = date1
    year_difference = 0
    while cur_date.year != date2.year:
        cur_date = date(cur_date.year + 1, cur_date.month, cur_date.day)
        year_difference += 1
        
    # now cur_date and date2 are on the same year, with potentially different dates
    fractional_year = abs((cur_date - date2).days) / 365
    
    return year_difference + fractional_year
​
​# option d1 function - same equation as wikipedia page
def fx_option_d1(strike, term, spot, volatility, domestic_rate, foreign_rate):
    """Calculate the d1 statistic for Garman Kohlhagen formula for fx option
    >>> '%.10f' % fx_option_d1(152, 91/365, 150, 0.13, 0.03, 0.04)
    '-0.2100058012'
    """
    d1 = (math.log(spot / strike) + ((domestic_rate - foreign_rate + (volatility**2) / 2)) * term) / (volatility * math.sqrt(term))
    return d1
​
# option d2 function - same equation as wikipedia page
def fx_option_d2(term, volatility, d1_option):
      """Calculate the d2 statistic for Garman Kolhagen formula for fx option
    >>> '%.10f' % fx_option_d2(91/365, 0.13, -0.21000580120118273)
    '-0.2749166990'
    """
    d2 = d1_option - (volatility * (math.sqrt(term)))
    return d2
​
# combine everything together into option price function
def fx_option_price(call, strike, expiration, spot_date, spot, volatility, domestic_rate, foreign_rate):
    """
    Calculates the fair price of a currency option.
    :param call:          True if this is a call option, False if this is a put option
    :param strike:        units of domestic currency per unit of foreign currency to be exchanged
    :param expiration:    date on which the exchange would take place if exercised
    :param spot_date:     date of valuation
    :param spot:          market exchange rate for fx exchanged on spot_date (same units as strike)
    :param volatility:    standard deviation of the logarithmic returns of holding this foreign currency (annualized)
    :param domestic_rate: simple risk-free interest rate from spot_date to expiration_date (annualized)
    :param foreign_rate:  simple risk-free interest rate from spot_date to expiration_date (annualized)
    :return:              option value in domestic currency for one unit of foreign currency
    
    """
    term = years_apart(spot_date, expiration)   # call years_apart function for term variable
    d1 = fx_option_d1(strike, term, spot, volatility, domestic_rate, foreign_rate)  # call d1 function
    d2 = fx_option_d2(term, volatility, d1)     # call d2 function
    domestic_discount = discount(domestic_rate, term)       # call discount function; domestic
    foreign_discount = discount(foreign_rate, term)   # call discount function; foreign
​
    if bool(call) == True:          # if call is true, use call option
        c = spot * foreign_discount * norm.cdf(d1) - (strike * domestic_discount * norm.cdf(d2))
        return c
    else:                           # if call is false, use put option
        p = (strike * domestic_discount * norm.cdf(-d2)) - (spot * foreign_discount * norm.cdf(-d1))
        return p
        

    
