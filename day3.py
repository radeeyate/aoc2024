import re

with open("./3.txt", "r") as f:
    f = f.read()

matches = re.findall(r'mul\(\d+,\d+\)', f)

p1 = 0

for match in matches:
    match = match.removeprefix("mul(").removesuffix(")").split(",")
    p1 += int(match[0]) * int(match[1])

print("part 1:", p1)

del matches

matches = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', f)
enabled = True
p2 = 0

print(matches)

for match in matches:

    if match == "don't()":
        enabled = False
    if match == "do()":
        enabled = True
    
    if enabled == True and match.startswith("mul"):
        match = match.removeprefix("mul(").removesuffix(")").split(",")
        p2 += int(match[0]) * int(match[1])
        enabled = True

print("part 2:", p2)
    