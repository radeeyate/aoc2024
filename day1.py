with open("./1.txt", "r") as f:
    f = f.read()

column1 = []
column2 = []

for line in f.splitlines():
    column1.append(line.split()[0])
    column2.append(line.split()[1])

#print(sorted(column1))
#print(sorted(column2))

part1 = 0
line = 0

for number in sorted(column1):
    number2 = sorted(column2)[line]
    #print(number, number2)
    distance = abs(int(number)-int(number2))
    #print(distance)
    part1 += distance
    line += 1


print("part 1:", part1)

part2 = 0

for number in column1:
    occurancesInRight = column2.count(number)
    score = int(number) * int(occurancesInRight)
    part2 += score

print("part 2:", part2)