symbolMenu = [['(','[','{','<'],[')',']','}','>'],[3,57,1197,25137]]
total = 0
f = open("input.txt", "r")
for line in f:
    line = line.strip()
    controlledLine = []
    sum = 0
    for i in range (len(line)):
        if line[i] in symbolMenu[0]:         # Opening character
            controlledLine.append(line[i])
        elif line[i] in symbolMenu[1]:         # Closing character
            location = symbolMenu[1].index(line[i])
            if controlledLine[-1] == symbolMenu[0][location]:    # Check if previous caracter is the belonging opening character.
                controlledLine.pop()
            else:
                sum = sum + int(symbolMenu[2][location])
                break
    total = total + sum
print("Total: ", total)