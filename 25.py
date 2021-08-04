fib = [1, 1]

for i in range(2, 100000):
    term = fib[i-1] + fib[i-2]
    fib.append(term)
    term = str(term)
    if len(term) == 1000:
        print(term)
        break

print(len(fib))