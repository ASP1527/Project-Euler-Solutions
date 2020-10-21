'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
num = [None] * 38
num[0] = 1
num[1] = 1
total = 0
for i in range(2, 38):
    num[i] = num[i-1] + num[i-2]
print(num)
numbers = []
for i in range(len(num)):
    if num[i] < 4000000:
        numbers.append(num[i])
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        total += numbers[i]
print(total)