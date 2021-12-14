foldedList = []
solution = []

def fold_paper(foldList, dotList):
    for i in range (len(foldList)):
        foldedList = []
        # Fold over x-line
        if foldList[i][0] == 'x':
            xFold = int(foldList[i][1])  # x-line
            for j in range (len(dotList)):
                currentDotX = int(dotList[j][0])
                if currentDotX > xFold:
                    xDiff = currentDotX - xFold
                    currentDotX = xFold - xDiff
                    newDot = [str(currentDotX), dotList[j][1]]
                    if newDot not in foldedList:   
                        foldedList.append(newDot)
                        dotList[j] = newDot
                else:
                    if dotList[j] not in foldedList:
                        foldedList.append(dotList[j])                      

        # Fold over y-line
        elif foldList[i][0] == 'y':
            yFold = int(foldList[i][1])  # y-line
            for j in range (len(dotList)):
                currentDotY = int(dotList[j][1])
                if currentDotY > yFold:
                    yDiff = currentDotY - yFold
                    currentDotY = yFold - yDiff
                    newDot = [dotList[j][0],str(currentDotY)]
                    if newDot not in foldedList:
                        foldedList.append(newDot)
                        dotList[j] = newDot          
                else:
                    if dotList[j] not in foldedList:
                        foldedList.append(dotList[j])

        dotList = foldedList
    see_paper(foldedList, xFold, yFold)

def see_paper(list, maxX, maxY):
    solution = []    
    for i in range (maxY):
        xString = []
        for j in range (maxX):
            xString.append(".")
        solution.append(xString)

    for i in range(len(list)):
        x = int(list[i][0])
        y = int(list[i][1])
        solution[y][x] = '#'
    
    for i in range (len(solution)):
        outString = ''
        for j in range (len(solution[0])):
            outString = outString + solution[i][j]
        print(outString)
            
def main():
    foldList = []
    dotList = []
    f = open("input.txt", "r")
    beforeSplit = True
    for line in f:
        if beforeSplit == True and line != '\n':
            dotList.append(line.strip().split(","))    

        elif beforeSplit == False:
            foldLine = line.strip().split("=")
            foldDir = foldLine[0][-1]
            foldValue = foldLine[1]
            foldList.append([foldDir, foldValue])

        if line == '\n':
            beforeSplit = False

    fold_paper(foldList, dotList)

if __name__ == "__main__":
    main()