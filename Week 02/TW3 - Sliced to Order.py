"""
TW3: Sliced to Order
Mohammed Elhaj
Sohrab Rajabi
Andrew Nalundasan

Teamwork exercise 3 code
"""

# user inputs
user_text = input('Enter some text, please: ')
start_position = int(input('Slice starting position (zero for beginning): '))
end_position = int(input('Slice ending position (can be negative to count from end): '))
stride = int(input('Stride: '))
print('Your text:', user_text)

# step 2: add delimiter '|'

slice = '|' + user_text[start_position:end_position:stride] + '|'

print('You want to slice it from', start_position, 'to', end_position,
      'which is', slice)

# step 3: setup prefix and suffix using slicing

prefix = '|' + user_text[:start_position:stride] + '|'
print('Prefix: ', prefix)
suffix = '|' + user_text[end_position::stride] + '|'
print('Suffix: ', suffix)

# step 4: put it all together

print(user_text[:start_position:stride] + '|' + user_text[start_position:end_position:stride]
      + '|' + user_text[end_position::stride])



