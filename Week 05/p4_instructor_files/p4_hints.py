### UP to the matching ### line, you might paste these lines near the top of each of your programs (after any imports)
# Which test case are we running?
# Change this line to switch to running a different test case
# (which is exactly what the grader will do and nothing more)
test_case = 1

# Following are instructor-provided files:
#   p4_testN_terms.csv:
#     line 1 column titles: term,inflation
#     line 2 values: term is number of months of annuity payments, inflation is annual inflation adjustment
#   p4_testN_cash_flows.csv:
#     column 1: number of months in the future
#     column 2: cash flow (US dollars) or interest rate (annual percentage simple rate)
#   p4_testN_interest_rates.csv:
#     column 1: number of months in the future
#     column 2: cash flow (US dollars) or interest rate (annual percentage simple rate)
annuity_terms_filename = 'p4_test%d_terms.csv' % test_case
sparse_cf_filename = 'p4_test%d_cash_flows.csv' % test_case
sparse_rates_filename = 'p4_test%d_interest_rates.csv' % test_case

# Following are the output files created by this program. These have one line for every month
dense_cf_filename = 'p4_test%d_dense_cf.txt' % test_case
dense_rates_filename = 'p4_test%d_dense_rates.txt' % test_case

# Get the annuity terms
terms_file = open(annuity_terms_filename, 'r')
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()
### End of section you want to paste into your programs



# Here is an example of computing a net present value (npv) of two cash flows
# This is hard-coded to show you how it works. Your code will be in loops using variables, etc.
from math import e  # place this import at the top of your file after the file's docstring
cf1 = 100000.00  # first cash flow is a receipt of $100k
term1 = 3        # in 3 months
rate1 = 4.3      # % interest rate per annum rate for a 3-month deposit
cf2 = -10000.00  # second cash flow is a payment of $10k
term2 = 6        # in 6 months
rate2 = 4.5      # % interest rate per annum rate for a 6-month deposit
npv = cf1 * e ** (-rate1 / 100 / 12 * term1) + cf2 * e ** (-rate2 / 100 / 12 * term2)



## Here is an example of reading from two files simultaneously, one line from each file at a time
# PLEASE use different (more apropos) variable names in your program
f1 = open(filename1, 'r')  # you supply the string variables, filename1 and filename2
f2 = open(filename2, 'r')
for line_from_f1, line_from_f2 in zip(f1, f2):
    f1_value = float(line_from_f1)  # assuming file1 and files are one-column bunches of textual numbers
    f2_value = float(line_from_f2)
    # NOW do some processing of the data for this line
f2.close()
f1.close()



## Here is an example of parsing a line from 2-column csv file (this is from the code above)
# of course the int/float conversion will depend on what you need to do in the given context
# PLEASE use apropos variable names for the given context
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)           # convert to an integer from a string
inflation = float(inflation) / 100.0       # convert to a float and ratio from a string with percent number



## Highlights of my p4_create_files.py
# Create the dense cash flow file
#     read the sparse file (2-columns), write the dense file (1-column, one line for each month)
#     the "missing" lines from the sparse file are 0.0 since there is no cash flow on those months
#     don't forget to close the files before you move on to the next section of code!
#     Here's our completed code for this! up to ### (Use this as a pattern for the interest rates dense file)
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
###
# Create the dense interest rates file
#     read the sparse file (2-columns), write the dense file (1-column, one line for each month)
#     the "missing" lines from the sparse file are a repeat of the previous line
#     don't forget to close



## Highlights of my p4_search_annuity.py
# First figure out the bracket: low can be $0, high can be total which we know is too high
#     While we're at it we can calculate the npv of the cash flows, since this won't change during the search
#     Here's the code in its entirety for this section!  (up to ###)
total = 0.0
cf_npv = 0.0
cf_file = open(dense_cf_filename, 'r')
rates_file = open(dense_rates_filename, 'r')
months = 1
for cf_line, rate_line in zip(cf_file, rates_file):
    rate = float(rate_line) / 12.0 / 100.0
    cash_flow = float(cf_line)
    total += cash_flow
    cf_npv += cash_flow * e ** (-rate * months)
    months += 1
cf_file.close()
print('Total customer-provided cash flows: $%.2f' % total)
print('NPV of customer-provided cash flows: $%.2f' % cf_npv)
lo, hi = 0.0, total
# Now we have a low that is too low and a high that is too high, so we can use bisection search
print('\nSearching for correct beginning monthly annuity payment:')
last_guess = lo
guess = hi  # which we will change to (lo + hi) / 2 in the loop
iter_count = 1  ### End of verbatim code

# the bisection search -- while the current guess is different than the last guess, keep narrowing it down
    ...
    # note that the guess is always rounded to decimal places since we want dollars and cents in USD
    guess = round(guess, 2)
    npv = cf_npv  # start npv at what we are getting from the customer-provided cash flows
    # then loop through the months figuring out how our annuity payments pv's deduct from the net present value
    ...
        # don't forget to adjust the payment every 12 months (when months % 12 == 0, right)
            payment += round(payment * inflation, 2)
    ...
    # after figuring out the npv at this payment guess, narrow the search range for the next time through the loop body
    if npv < 0.0:
        # too high a monthly payment
        hi = guess
    else:
        # too low a monthly payment
        lo = guess
# Finally, print out the details of the payments every year



# !!!
# Remember to look at p4_test1_results.txt -- that is the expected output from running the search program on test case 1
