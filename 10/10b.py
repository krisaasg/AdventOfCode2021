symbolMenu = [['(','[','{','<'],[')',']','}','>'],[3,57,1197,25137],[1,2,3,4]]
incompleteLine = []
results = []
total = 0
f = open("input.txt", "r")
for line in f:
    line = line.strip()
    controlledLine = []
    sum = 0
    i = 0
    corrupted = False
    while corrupted == False and i < len(line):
        if line[i] in symbolMenu[0]:         # Opening character
            controlledLine.append(line[i])
            if i == len(line) - 1 and len(controlledLine) > 0:
                    incompleteLine.append(controlledLine) 
        elif line[i] in symbolMenu[1]:         # Closing character
            location = symbolMenu[1].index(line[i])
            if controlledLine[-1] == symbolMenu[0][location]:    # Check if previous caracter is the belonging opening character.
                controlledLine.pop()
                if i == len(line) -1 and len(controlledLine) > 0:
                    incompleteLine.append(controlledLine) 
            else:
                sum = sum + int(symbolMenu[2][location])
                corrupted = True
        i += 1
    total = total + sum

print("Solution 10a: ", total)

for i in range (len(incompleteLine)):
    incompleteLine[i].reverse()
    score = 0
    for j in range(len(incompleteLine[i])):
        location = symbolMenu[0].index(incompleteLine[i][j])
        symbolValue = symbolMenu[3][location]
        score = (score * 5) + symbolValue
    results.append(score)
results.sort()
mIndex = int((len(results)-1)/2)
print("Winner is: ", results[mIndex] )