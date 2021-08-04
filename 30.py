'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

array = []

for i in range(2, 5*9**5): #6*9**5 is the limit for the largest 5 digit number for which this formula is possible
    n = i
    temp = 0
    n = str(n)
    exp = 5
    for j in range(len(n)):
        t = n[j]
        t = int(t)
        temp += (t ** 5)
    if temp == i:
        array.append(temp)
        

print(array)
sum = 0

for i in range(len(array)):
    sum += array[i]

print(sum)