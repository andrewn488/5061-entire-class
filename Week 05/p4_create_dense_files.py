"""P4: Data Translator
Pass 1: p4_create_dense_files
via Test Case 1
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
Date: 10/17/2020
"""

# import needed e from math
from math import e
##import os
##os.getswd()

# identify test case
test_case = 1

# inputs, knowns, and variables; provided from instructor files
annuity_terms_filename = 'p4_test%d_terms.csv' % test_case
sparse_cf_filename = 'p4_test%d_cash_flows.csv' % test_case
sparse_rates_filename = 'p4_test%d_interest_rates.csv' % test_case

# output files
dense_cf_filename = 'p4_test%d_dense_cf.txt' % test_case
dense_rates_filename = 'p4_test%d_dense_rates.txt' % test_case

# get the annuity terms
terms_file = open(annuity_terms_filename, 'r')
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()

# create file for dense cash flow
# 1: read sparse file (2 columns)
# 2: write dense file (one line for each month, 1 column)

sparse_file = open(sparse_cf_filename, 'r')
dense_file = open(dense_cf_filename, 'w')
month = 1
for line in sparse_file:
    cf_month = line.split(',')
    cf_amount = line.split(',')
    cf_month = int(cf_month)        # converting str to int
    cf_amount= float(cf_amount)     # convert str to float
    while month < cf_month:
        dense_file.write(str(0.0) + '\n')       # 0.0 means 'zero cash flow this month'
        month += 1
    dense_file.write(str(cf_amount) + '\n')     # cash flow month
    month += 1
sparse_file.close()
dense_file.close()






