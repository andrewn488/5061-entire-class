"""
Week 3 class exercises
Warmups, non-graded assignments, and practice
9/29/2020
Andrew Nalundasan
"""

#n = int(input('Enter number: '))

#while n > 0: 
   # print('hello')
   # n -= 1


#x = int(input('Enter number: '))
#while x != 100:
 #   print(x)
  #  x += 1
#print('Done')


#num = int(input('enter a positive odd integer: '))
#while not (num > 0 and num % 2 != 0):
 #   num = int(input('must be positive and odd: '))

#print('enter number to multiply, 1 to end')
#product = 1.0
#num = float(input('enter num: '))
#while num != 1:
 #   product *= num
  #  num = float(input('enter num: '))
#print(product)

#x = range(1000, 100, -5)
#for n in x:
 #   print(n)

#for letter in 'Can\'t say':
 #   print(letter)

# While Loop - Some String
#s = 'some string'
#i = 0
#while i < len(s):
  #  letter = s[i]
  #  print(letter)
  #  i += 1

# For Loop - Some String
#s = 'some string'
#for letter in s:
#    print(letter)

# While Loop - n times
#n = int(input('n: '))
#i = 0
#while i < n:
#    print('hello')
#    i += 1

# For Loop - n times
#n = int(input('n: '))
#for i in range(n):
#    print('hello')

# While Loop - low/high
#lo = int(input('low: '))
#hi = int(input('high: '))
#i = lo
#while i <= hi:
#    print(i)
#    i += 3

# For Loop - low/high
#lo = int(input('low: '))
#hi = int(input('high: '))
#for i in range(lo,hi + 1, 3):
#    print(i)

#r = range(3, 10, 2)
# a - range(3, 10, 2)
# b - 4
# c - 7
# d - 9
# e - range(5, 9, 2)
# f - range(3, 7, 2)
# g - True
# h
#for i in r:
#    print(i)

# PQ2

alphabet = 'abcdefg'
k = 3
i = 2
#print(alphabet[0])
#print(alphabet[3])
#print(alphabet[i])
#print(alphabet[(i + k) // 2])
#print(alphabet[2:5])
#print(alphabet[i:i + 3])
#print(alphabet[i:i + k])
#for i in range(5):
#    print(i, i + k)
#for i in range(len(alphabet) - k + 1):
#    print(i)
for i in range(len(alphabet) - k + 1):
    print(alphabet[i:i + k])
