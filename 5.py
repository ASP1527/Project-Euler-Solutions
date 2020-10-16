'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?     
'''
numbers = []

for j in range(20, 300000000):
    count = 0
    for i in range(1, 21):
        if j % i == 0:
            count += 1
    if count == 20:
        numbers.append(j)

print(numbers[0])
