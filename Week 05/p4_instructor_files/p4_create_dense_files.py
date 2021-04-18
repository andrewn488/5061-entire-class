"""P4: Data Translator
Pass 1: p4_create_dense_files
via Test Case 1
Author: Andrew Nalundasan
Collaboration: Sohrab Rajabi, Giridharan Vivek Kandadai, Arunima Roy, Brittney Cherry
For: OMSBA 5061, Seattle University
Date: 10/18/2020
"""

#import needed e from math
from math import e

#identify which test case this is
test_case = 1

#associate variable names to the instructor provided files
annuity_terms_filename = 'p4_test%d_terms.csv' % test_case
sparse_cf_filename = 'p4_test%d_cash_flows.csv' % test_case
sparse_rates_filename = 'p4_test%d_interest_rates.csv' % test_case

#output files
dense_cf_filename = 'p4_test%d_dense_cf.txt' % test_case
dense_rates_filename = 'p4_test%d_dense_rates.txt' % test_case

#annuity terms
terms_file = open(annuity_terms_filename, 'r')
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()

# Create the dense cash flow file
sparse_file = open(sparse_cf_filename, 'r')
dense_file = open(dense_cf_filename, 'w')
month = 1
for line in sparse_file:
    cf_month, cf_amount = line.split(',')
    cf_month = int(cf_month)  # convert the string cf_month into an integer
    cf_amount = float(cf_amount)  # convert the string cf_amount into a float
    while month < cf_month:
        dense_file.write(str(0.0) + '\n')  # no cash flows for this month
        month += 1
    dense_file.write(str(cf_amount) + '\n') # here's the cash flow month
    month += 1
while month <= annuity_term:  # any later months until the end of the annuity term after last cash flow
    dense_file.write(str(0.0) + '\n')
    month += 1
sparse_file.close()
dense_file.close()
# Create the dense interest rates file
sparse_file = open(sparse_rates_filename, 'r')
dense_file = open(dense_rates_filename, 'w')
month = 1
i = ''
for line in sparse_file:
    rates_month, rates_amount = line.split(',')
    rates_month = int(rates_month)  # convert the string rates_month into an integer
    rates_amount = float(rates_amount)  # convert the string rates_amount into a float
    while month < rates_month:# find missing rates amounts
        dense_file.write(str(i) + '\n')
        month += 1
    dense_file.write(str(rates_amount) + '\n') # write the rate for missing months to the dense file
    month += 1
    i = (rates_amount)
while month <= annuity_term:  # any later months until the end of the annuity term after last inputted rate will have rate of 1.9
    dense_file.write(str(i) + '\n')
    month += 1
sparse_file.close()
dense_file.close()


