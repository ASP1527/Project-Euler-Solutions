'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

with open('22.txt', 'r') as f:
    names = f.read().replace('"', '').split(",")
f.close()

names = sorted(names)

total = 0

name = names[0]

print(name, ord(name[0])-64)

for i in range(len(names)):
    totalName = 0
    name = names[i]
    for j in range(len(name)):
        totalName += ord(name[j])-64
    total = total + (totalName * (i + 1))

print(total)
