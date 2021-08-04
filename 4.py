'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindromes = []

for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        stringProduct = str(product)
        reverse = stringProduct[::-1]
        reverse = int(reverse)
        if reverse == product:
            palindromes.append(product)

p1 = palindromes[0]

for i in range(1, len(palindromes)):
    if palindromes[i] > p1:
        p1 = palindromes[i]

print(p1)
