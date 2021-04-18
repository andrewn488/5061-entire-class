"""Midterm practice
10/28/2020
"""
# q1
def practice_01(seq):
    count = 0
    for i in seq:
        if i % 3 == 0:
            count += 1
    return count

# q2
def practice_02(seq):
    count = 0
    for elem in seq:
        if type(elem) is int:
            count +=1
    return count

# q3
def practice_03(seq):
    count = 0
    for elem in seq:
        if elem[0:1] == 'a':
            count += 1
    return count

# q4
def practice_04(seq, suffix):
    count = 0
    for elem in seq:
        if suffix in elem:
            count += 1
    return count

# q5
def practice_05(seq, sub_string):
    count = 0
    for elem in seq:
        if type(elem) == str:
            if sub_string in elem:
                count += 1
    return count

# q6
def practice_06(seq, sub_string):
    my_list = []
    for elem in seq:
        if type(elem) == str:
            if sub_string in elem:
                my_list.append(elem)
    return my_list

# q7
def practice_07(my_dictionary):
    values = my_dictionary.values()
    return values

# q8
def practice_08(my_dictionary):
    keys = my_dictionary.keys()
    return keys

# q9
def practice_09(my_dict):
    values = type(my_dict.values())
    return values

# q 10
def practice_10(my_dict):
    my_list = []
    for elem in my_dict:
        elem = type(my_dict.keys())
        my_list += elem
    return my_list

# q11
def practice_11(my_dict):
    count = 0
    for word in my_dict:
        if type(word) is int:
            count += 1
    return count

# q12
def practice_12(my_dict, num):
    my_list = []
    for values in my_dict:
        if type(my_dict.values) is int:
            if my_dict.values / num == 0:
                my_list += my_dict.values
    return my_list

# q20
my_dict = {1: 5, 2: 55, 3: 21, 4: 105, 5: 44}
def practice_20(my_dict):
    if my_dict.values() % 5 == 0:
        divisible_by_5 == True
    else:
        divisible_by_5 == False
    return divisible_by_5

# tracing
def f(a, b, c, k=15):
    result = ""
    for i in range(a, b, c):
        if len(result) + len(str(i)) + 1 > k:
            result += "..., "
            break
        result += str(i) + ", "
    return result[:-2]  # take off ", " from end

def g(a):
    b = 1000
    return f(b, b + a, 3)

words = ['hello', 'goodbye']
ret = []
for word in words:
    if len(word) >= 3:
        ret.append(word[-3:])
    print(ret)

def with_mean(x):
    total_sum = 0
    count = 0
    new_x = x
    for element in new_x:
        total_sum += element
        count += 1
        avg = total_sum / count
        new_x.append(avg)
    return new_x

def sortedValues(my_dict):
    sorted_vals = ()
    sorted_keys = sorted(my_dict())
    for element in sorted_keys:
        element = sorted_keys.values()
        sorted_vals += (element,)
    return sorted_vals


##file_name = input('What is the filename?' )
##file_name = open('question_9.txt', 'w')
##file_name.write(input())
##
##file_name.close
##    
##    
##my_dict = {'cat': 'An animal that meows all the time.',
## 'dog': 'A barker.',
## 'elk': 'The elk is a magnificent animal that lives in the woods.'}


    

