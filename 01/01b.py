line1 = 0
line2 = 0
line3 = 0
previousWindowSum = 0
currentwindowSum = 0
counter = 0
f = open("input.txt", "r")
for line in f:
    line1 = line2
    line2 = line3
    line3 = int(line)

    if line1 and line3:
        currentWindowSum = line1 + line2 + line3
        #print(int(currentWindowSum))
        if currentWindowSum > previousWindowSum > 0:
            counter = counter + 1
            #print("(increased)")
        previousWindowSum = currentWindowSum

print(counter)