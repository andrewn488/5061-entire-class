"""
FINAL Exam prep
"""

# midterm 2 - question 7
def sumEvenKeyedValues(dict):
    total_sum = 0
    for keys in dict:
        if keys % 2 == 0:
            total_sum += dict[keys]
    return total_sum


# midterm 2 - question 8
def catKeys(dict):
    ret = ''
    for key in dict:
        ret += str(key)
    return ret


# midterm 2 - question 9
def processFile(f):
    file = open(f, 'r')

    d = {}
    for line in file:
        line_elements = line.split(' ')
        if len(line_elements) < 3:
            continue
        key = line_elements[0]
        val_1 = float(line_elements[1])
        val_2 = float(line_elements[2])
        if key in d:
            continue

        d[key] = val_1 * val_2

    d.sorted()
    file.close()
    return d


##file = open('example.txt', 'r')
##
##my_dict = {}
##elem = file.readline()
##print(elem)
##key, val_1, val_2 = elem.split(' ')
##val_1 = float(val_1)
##val_2 = float(val_2)
##my_dict[key] = val_1 * val_2 
    
