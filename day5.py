with open("./5.txt", "r") as f:
    f = f.read()

rulesStr, updatesStr = f.strip().split("\n\n")

rules = {}
p1 = 0
updates = []
p2 = 0

for line in rulesStr.splitlines():
    first, second = line.split("|")
    first, second = int(first), int(second)
    rules.setdefault(first, []).append(second)

for line in updatesStr.splitlines():
    updateNums = []
    for num in line.split(","):
        updateNums.append(int(num))
    updates.append(updateNums)
    del updateNums

for update in updates:
    violation = False
    for page in update:
        trimmedUpdate = update[:update.index(page)]
        try:
            rulesForPage = rules[page]
        except:
            break

        for rule in rulesForPage:
            if rule in trimmedUpdate:
                violation = True
                break
    if violation == False:
        p1 += update[(len(update)) // 2]
    else:
        orderedUpdate = []
        for page in update:
            inserted = False
            for i, existingPage in enumerate(orderedUpdate):
                if existingPage in rules and page in rules[existingPage]:
                    orderedUpdate.insert(i, page)
                    inserted = True
                    break
            if not inserted:
                orderedUpdate.append(page)

        p2 += orderedUpdate[(len(orderedUpdate)) // 2]

print("part 1:", p1)
print("Part 2:", p2)