nUnique = [0]*10
f = open ("input.txt", "r")
for line in f:
    subString = line.split("| ")[1]
    subList = subString.split()
    for i in range(0, len(subList)):
        nUnique[len(subList[i])] += 1
sum = nUnique[2] + nUnique[3] + nUnique[4] + nUnique[7]
print(sum)