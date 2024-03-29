'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
x = 100
answer = 0
for i in range(1, x):
    if i == 1:
        answer = x * i
    else:
        answer *= i

answer = str(answer)
total = 0

for i in range(len(answer)):
    total += int(answer[i])

print(total)