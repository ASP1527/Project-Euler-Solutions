sum = 0

for i in range(3, 1500000): #4143 is the sum of factorials up to 9
    total = 0
    n = str(i)
    for j in range(len(n)):
        digit = int(n[j])
        multiply = 1
        for k in range(1, digit+1):
            multiply *= k
        total += multiply
    if total == i:
        sum += total

print(sum)