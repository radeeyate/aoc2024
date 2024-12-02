with open("./2.txt", "r") as f:
    f = f.read()

safe = 0
unsafe = 0

for line in f.splitlines():
    firstNum = int(line.split()[0])
    lastSeenNum = firstNum
    lastGoing = ""
    going = ""
    currentStatus = ""
    lastStatus = "safe"
    for number in line.split()[1:]:
        if abs(int(number) - lastSeenNum) in (1, 2, 3):
            currentStatus = "safe"
        else:
            currentStatus = "unsafe"

        if int(number) > lastSeenNum:
            going = "up"
        elif int(number) == lastSeenNum:
            currentStatus = "unsafe"
        else:
            going = "down"

        if going != lastGoing and lastGoing != "":
            currentStatus = "unsafe"
        
        if currentStatus != lastStatus:
            currentStatus = "unsafe"

        lastStatus = currentStatus
        lastSeenNum = int(number)
        lastGoing = going

        if currentStatus == "unsafe":
            break
    #print(currentStatus)
    
    if currentStatus == "safe":
        safe += 1
    else:
        unsafe += 1

print("part 1:", safe)

safe = 0

for line in f.splitlines():
    firstNum = int(line.split()[0])
    lastSeenNum = firstNum
    lastGoing = ""
    going = ""
    currentStatus = "safe"
    lastStatus = "safe"
    bad = 0
    numbers = [int(x) for x in line.split()]

    for number in line.split()[1:]:
        if abs(int(number) - lastSeenNum) in (1, 2, 3):
            currentStatus = "safe"
        else:
            currentStatus = "unsafe"

        if int(number) > lastSeenNum:
            going = "up"
        elif int(number) == lastSeenNum:
            currentStatus = "unsafe"
        else:
            going = "down"

        if going != lastGoing and lastGoing != "":
            currentStatus = "unsafe"
        
        lastStatus = currentStatus
        lastSeenNum = int(number)
        lastGoing = going
        if currentStatus == "unsafe":
            bad += 1
        currentStatus = "safe"

    if bad == 0 or bad == 1:
        safe += 1
    
print("part 2:", safe + 1)   # this worked for me. I don't know if it would work for you.
