'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

m = 5
n = 2

found = False

while not(found):
    m += 4
    n += 2
    a = 2 * m * n
    b = m^2 - n^2
    c = m^2 + n^2
    if a + b + c == 1000:
        print(a, b, c)
        found = True