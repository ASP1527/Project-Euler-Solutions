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
