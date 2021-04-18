"""G5: Structured Types
Author: Andrew Nalundasan
For: OMSBA 5061, Seattle University
Date: 10/17/2020
"""
# q1
# foo = (1, 2, 2) - YES
foo = ()
foo.append(1)
foo.append(2)
foo.append(2)
# foo = (1, 2) - YES
##foo = () + (1, 2) + (2) - NO
##foo = (1) + (2) + (2) - NO
#foo = () - YES
#foo = foo + (1, 2, 3)
#foo += (4, 5, 4, 3, 2)
print(foo[0], foo[1], foo[-1])

#q2
##a = [1, 2, 3]
##b = a
##a.append(4)
##
##4 == b[3]

#q3
##a = (1, 2, 3)
##b = a
##c = (1, 2, 3)
##a += (4,)

#q4
##a = {'first':1, 'second':2, 'third':3}
###x = a - NO CLONE
###x = dict(a) -YES CLONE
####x = {} - YES CLONE
####for key in a:
####    x[key] = a[key]
##
##x = {key:a[key] for key in a}

#q5
#a = [3.4, -1.6, -14, -233.33e2]

##b = [] - YES
##for elem in a:
##    b.append(abs(elem))
##a = b

##a = [value for value in map(abs, a)] - YES

##def applyToAll(f, a): - YES
##    b = []
##    for elem in a:
##        b.append(f(elem))
##    return b
##a = applyToAll(abs, a)

##def applytToAll(f, a): - NO
##    b = []
##    for elem in a:
##        b.append(f(elem))
##    return b
##a = applyToAll(lambda x : abs(x), a)
