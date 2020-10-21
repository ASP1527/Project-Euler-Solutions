'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

x = 2
count = 1
prime = []
for i in range(1, 9):
    if i == 1:
        prime.append(2)
    numcount = 0
    x += 1
    for i in range(1, x):
        if x % i == 0:
            numcount += 1
    if numcount == 1:
        prime.append(x)

print(prime)

answer = 0

for i in range(len(prime)):
    answer += prime[i]

print(answer)
