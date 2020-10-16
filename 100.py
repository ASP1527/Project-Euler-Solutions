b = 15
n = 21

while n < 1000:
    if (b**2 - b - n**2 + n) == 0:
        print(b, n)
    b += 1
    n += 1