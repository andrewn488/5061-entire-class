"""TW6: File Play
Exercise: inputToFile
Team: Tam Tamura, Austin Bednar, Andrew Nalundasan
For: OMSBA 5061, Seattle University
Date: 10/14/2020
"""

# q1
def inputToFile(tw6_patos):
    """gathering inputs for the numbers file"""
    print('Enter a series of numbers')
    print("Type the word 'DONE' by itself to indicate when you're finished")
    user_input = input('first line: ')
    tw6_patos = open(tw6_patos, 'w')     # this is where you can start writing
    
    while user_input != 'DONE':
        tw6_patos.write(user_input + '\n')
        user_input = input('next line: ')       # each line is written in the file
    tw6_patos.close()      # this closes the file
 now go open the file in windows explorer. it's like magic

# Q2
file_name = open(input('Enter file name: '), 'r')       # call the 'read' method for an existing file
search_string = input('Enter a string: ')
def searchFile(file_name, search_string):
    """User to enter a string to search for in file"""
    counter = 0
    for line in file_name:
        for word in line:
            for string in word:
                if string == search_string:
                    counter += 1
    print(f'There are {counter} number of {search_string} in your file')
    file_name.close()


# q3
def sumFile(tw6_patos):
    """get the highest, lowest, and total of the numbers in the file"""
    file = open(tw6_patos, 'r')
    highest = -1000000
    lowest = 1000000
    total = 0
    for line in file:
        number = float(line)
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
        total += number
    return(lowest, highest, total)

# q4

def tw6(filename):
    """combine all our functions together"""
    print('Enter 5 numbers')
    for i in range(5):
        print(input('Enter another number: '))
    inputToFile('last_question.txt')
    searchFile(filename, '\n')
    sumFile(filename)
filename = 'last_question.txt'    
