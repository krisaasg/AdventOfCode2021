previousLine = ""
counter = 0
f = open("input.txt", "r")
for currentLine in f:
    if currentLine > previousLine:
        counter = counter + 1
    previousLine = currentLine
print(counter)