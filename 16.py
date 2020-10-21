'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

n = 2 ** 1000
print(n)
total = 0
numberStr = str(n)
for i in range(len(numberStr)):
    total += int(numberStr[i])
print(total)
