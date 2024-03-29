'''
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
'''
square = 0
for i in range(1,101):
  square = square + i * i

naturalnum = 0
for n in range (1,101):
  naturalnum = naturalnum + n

naturalnum = naturalnum * naturalnum

difference = naturalnum - square

print (difference)