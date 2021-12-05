intList = []
tmpList = []
vertList = []
horiList = []
diagList = []
resultList = [ [0]*1000 for n in range(1000) ]

f = open ("input.txt", "r")
for line in f:
    tmpText = line
    tmpText = tmpText.replace(" -> ", ",")
    tmpText = tmpText.strip()
    tmpList = tmpText.split(",")
    for i in range(0, len(tmpList)):
        tmpList[i] = int(tmpList[i])
    intList.append(tmpList)
    tmpList = []

# Makes list 2D only, and splits into horiList[], vertList[] and diagList
i = 0
while i < len(intList):
    if intList[i][0] == intList[i][2]:
        if intList[i][1] > intList[i][3]:
            horiList.append(intList[i])
        else: # Arranging coordinates with highest value coordinate pair first.
            tmpList.append(intList[i][2])
            tmpList.append(intList[i][3])
            tmpList.append(intList[i][0])
            tmpList.append(intList[i][1])
            horiList.append(tmpList)
            tmpList = []

    elif intList[i][1] == intList[i][3]:
        if intList[i][0] > intList[i][2]:
            vertList.append(intList[i])
        else:
            tmpList.append(intList[i][2])
            tmpList.append(intList[i][3])
            tmpList.append(intList[i][0])
            tmpList.append(intList[i][1])
            vertList.append(tmpList)
            tmpList = []
    else:
        # Diagonal line
        if intList[i][1] > intList[i][3]:
            diagList.append(intList[i])
        else:
            tmpList.append(intList[i][2])
            tmpList.append(intList[i][3])
            tmpList.append(intList[i][0])
            tmpList.append(intList[i][1])
            diagList.append(tmpList)
            tmpList = []

    i += 1

# Iterates through lists and adds 1 to coordinates that are affected
i = 0
j = 0
while i < len(horiList):
    diff = horiList[i][1] - horiList[i][3]
    while j <= diff:
        x = horiList[i][0]
        y = horiList[i][1] - j
        resultList[x][y] = resultList[x][y] + 1
        j += 1
    i += 1
    j = 0

# Vertlist
i = 0
j = 0
while i < len(vertList):
    diff = vertList[i][0] - vertList[i][2]
    while j <= diff:
        x = vertList[i][0] - j
        y = vertList[i][1]
        resultList[x][y] = resultList[x][y] + 1
        j += 1
    i += 1
    j = 0

# Diaglist
i = 0
j = 0
while i < len(diagList):
    diff = diagList[i][1] - diagList[i][3]
    while j <= diff:
        if diagList[i][0] > diagList[i][2]:
            x = diagList[i][0] - j
            y = diagList[i][1] - j
        else:
            x = diagList[i][0] + j
            y = diagList[i][1] - j
        resultList[x][y] = resultList[x][y] + 1
        j += 1
    i += 1
    j = 0


# Iterates over resultList to find number of coordinates with 2 or more lines
i = 0
j = 0
counter = 0
while i < len(resultList):
    while j < len(resultList[i]):
        if resultList[i][j] > 1:
            counter += 1
        j += 1
    i += 1
    j = 0
print("Result: ", counter)