'''
def shift(q):
    q = str(q)
    x = (q[1:] + q[:1])
    return int(x)

def isPrime(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

count = 0

for i in range(2, 1000000):
    n = i
    prime = isPrime(n)
    p = 0
    while prime and p <= n:
        n = shift(n)
        #print(n)
        prime = isPrime(n)
        p += 1
    if prime:
        count +=1

print(count)
'''

def SieveOfEratosthenes(n):
    primeList = []
    primes = [True for i in range(n+1)] #sets all items in list to false
    primes[0] = False #sets 1 & 0 to false as they're not prime
    primes[1] = False
    p = 2 #starts at 2
    while p ** 2 <= n: #loops through until the end of the list
        if primes[p] == True: #checks if the number has not been flagged as not prime
            for i in range(p+p, n+1, p): #every pth number is set to non prime as they are a multiple of p
                primes[i] = False
        p += 1
    return primes

primeList = SieveOfEratosthenes(1000000)
count = 0

for i in range(0, 1000000):
    num = i
    isPrime = True
    n = str(num)
    n1 = str(num)
    for j in range(0,len(n1)):
        n = int(n)
        if primeList[n]:
            n = str(n)
            n = n[1:] + n[:1]
        else:
            isPrime = False
            break
    if isPrime:
        num = str(num)
        if not("0" in num):
            count += 1

    
print(count)
