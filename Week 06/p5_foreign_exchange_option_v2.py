

import math

# years_apart function
from datetime import date
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

    # make certain that date1 is prior to date2
    if date2 < date1:
        date1, date2 = date2, date1
    cur_date = date1
    year_difference = 0
    while cur_date.year != date2.year:
        cur_date = date(cur_date.year + 1, cur_date.month, cur_date.day)
        year_difference += 1
    # now cur_date and date2 are on the same year, with potentially different dates
    fractional_year = abs((cur_date - date2).days) / 365
    return year_difference + fractional_year

x = years_apart(date(1959, 10, 1), date(2019, 6, 2))
print(x)

# discount function
def discount(rate, term):
    """Calculate the discount factor for given simple interest rate and term.
    present_value = future_value * discount(rate, term)
    >>> discount(0.123, 0.0)
    1.0
    >>> discount(0.03, 2.1)
    0.9389434736891332
    """
    discount = math.exp(-rate * term)
    return discount

# functiona to calculate d1
def fx_option_d1(strike, term, spot, volatility, domestic_rate, foreign_rate):
    """Calculate the d1 statistic for Garman Kohlhagen formula for
    fx option """
    from math import sqrt, exp, log, pi
##    from scipy.stats import norm
    d1 = (log(spot/strike) + ((domestic_rate - foreign_rate + (volatility**2)/2)) * term)/(volatility*sqrt(term))
    print(d1)
    return d1

d1 = '%.10f' % fx_option_d1(152, 91/365, 150, 0.13, 0.03, 0.04)
print(d1)


# function to calculate d2
def fx_option_d2(term, volatility, d1):
    """Calculate the d2 statistic for Garman Kolhagen formula for fx option
    >>> '%.10f' % fx_option_d2(91/365, 0.13, -0.21000580120118273)
    '-0.2749166990'
    """
    from math import sqrt, exp, log, pi
##    from scipy.stats import norm
    d2 = d1 - (volatility * sqrt(term))
    print(d2)
    return d2

# big kahuna

def fx_option_price(call, strike, expiration, spot_date, spot,
                    volatility, domestic_rate, foreign_rate):
    from math import e
    from scipy.stats import norm
    term = 91/365
    #call = fx_option_price(0,)
    p = 0
    domestic_discount = discount(domestic_rate, term)
    foreign_discount = discount(foreign_rate, term)
    d1 = fx_option_d1(strike, term, spot, volatility, domestic_rate, foreign_rate...
    d2 = fx_option_d2(term, volatility, d1)
    if bool(call) == True:
        call = (spot * discount(foreign_rate, term) * norm.cdf(d1)) - strike * (discount(domestic_rate, term) * norm.cdf(d2)) 
        return call
    else:
        put = (strike * discount(domestic_rate, term) * norm.cdf(-d2)) - (spot * discount(foreign_rate, term) * norm.cdf(-d1))
        return put
