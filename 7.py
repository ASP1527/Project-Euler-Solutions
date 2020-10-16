'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
x = 2
count = 1
prime = []
while len(prime) < 10001:
    if count == 1:
        prime.append(2)
        count += 1
    numcount = 0
    x += 1
    for i in range(1, x):
        if x % i == 0:
            numcount += 1
    if numcount == 1:
        prime.append(x)

print(prime[10000])