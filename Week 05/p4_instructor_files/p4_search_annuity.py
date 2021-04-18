"""P4: Data Translator
Pass 2: p4_search_annuity
via Test Case 1
Author: Andrew Nalundasan
Collaboration: Sohrab Rajabi, Giridharan Vivek Kandadai, Arunima Roy, Brittney Cherry
For: OMSBA 5061, Seattle University
Date: 10/17/2020
"""
# Import needed e from math
from math import e 

# Import the create dense files 
from p4_create_dense_files import inflation, annuity_term

test_case = 1
dense_cf_filename = 'p4_test%d_dense_cf.txt' % test_case
dense_rates_filename = 'p4_test%d_dense_rates.txt' % test_case

total = 0.0
cf_npv = 0.0
cf_file = open(dense_cf_filename, 'r') # opens the file
rates_file = open(dense_rates_filename, 'r') #opens the file
months = 1
for cf_line, rate_line in zip(cf_file, rates_file):
    rate = float(rate_line) / 12.0 / 100.0 # change the rate
    cash_flow = float(cf_line)
    total += cash_flow
    cf_npv += cash_flow * e ** (-rate * months) # calculates the cashflow * discount rate
    months += 1
cf_file.close()
print('Total customer-provided cash flows: $%.2f' % total)
print('NPV of customer-provided cash flows: $%.2f' % cf_npv)
lo, hi = 0.0, total
print('\nSearching for correct beginning monthly annuity payment:')
last_guess = lo
guess = hi  
iter_count = 1

ttl_npv = 0
for months in range(annuity_term):
    months = 1
    rates_file = open(dense_rates_filename, 'r')
    guess = round(((lo + hi) / 2),2)
    pmt = guess
    for rate_line in rates_file:
        rate = float(rate_line) / 12.0 / 100.0 # gets rate
        disc = e ** (-rate * months) # gets discount rate
        pmt_npv = disc * pmt # gets the payment amount
        # Following if statements are ways to calculate the total NPV
        if months == 1:
            ttl_npv = cf_npv - pmt_npv 
        else:
            ttl_npv = ttl_npv - pmt_npv
        if months % 12 == 0:
            pmt += round(pmt * inflation, 2) # takes into account inflation after every year
        months += 1
    last_guess = guess
    if ttl_npv < 0.0:
        hi = guess
    else:
        lo = guess
    print(f'{iter_count}: With annuity of ({lo} + {hi})/2 = {round(guess,2)}, NPV is ${round(ttl_npv, 2)}')
    iter_count += 1
 

print(f'\nFirst year pay ${guess} per month')
print(f'For a total of ${guess * round(annuity_term,2)}')


print('=' * 41)
print('Details of the customer NPV calculations:')
print('=' * 41)

cf_file = open(dense_cf_filename, 'r')
rates_file = open(dense_rates_filename, 'r')
count = 1
for cf, rate_line in zip(cf_file, rates_file):
    if float(cf) != 0.0:
        rate = float(rate_line) / 12.0 / 100.0
        print(f'months: {count} cashflow: {float(cf)} discount: {(e ** (-rate * count))} npv: {float(cf) * (e ** (-rate * count))}') 
    count += 1
print('Total customer-provided cash flows: $%.2f' % total)
print('NPV of customer-provided cash flows: $%.2f' % cf_npv)
