'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

num = 600851475143 
prime = []

factorlist = []
for i in range(1, num + 1):
  if num % i == 0:
    factorlist.append(i)
print (factorlist)
for j in range(len(factorlist)):
    numcount = 0
    x = factorlist[j]
    for i in range(1, x):
        if x % i == 0:
            numcount += 1
    if numcount == 1:
        prime.append(x)

print(prime[-1])