def check_tables(polledInn, boardsInn):
    # Sjkke om table vinner og i så fall kalkulere sum.
    #print(polledInn)
    winner = False
    i = 0
    while i < len(boardsInn):
        if winner == False:
            row = 0
            column = 0
            tempList = []
            for j in range(5):
                tempRow = boardsInn[(i+j)].split()
                tempList.append(tempRow)
                #tempList.append(boardsInn[i])
            #print(tempList[1][1])
            
            sumFound = 0
            sumUnmarked = 0
            #winningNumber = 0
            
            while row < 5:
                column = 0
                sumFound = 0
                while column < 5:
                    if tempList[row][column] in polledInn:
                        sumFound += 1
                    else:
                        sumUnmarked = sumUnmarked + int(tempList[row][column])
                    column += 1
                if sumFound == 5:
                    winner = True
                    #winningNumber = 
                    print("Winner")
                sumFound = 0
                row += 1

            column = 0
            while column < 5:
                row = 0
                while row < 5:
                    if tempList[row][column] in polledInn:
                        sumFound += 1
                    row += 1
                    if sumFound == 5:
                        winner = True
                        print("Winner")
                sumFound = 0
                column += 1
            
            if winner == True:
                # Summere alle umerkede, gange med nummer som utløste seier (siste nummer i polledInn)
                print(sumUnmarked)
                print(polledInn[-1])
                points = sumUnmarked * int(polledInn[-1])
                print("Winning value: ", points)

            #print(i)
            i += 6
    #print("Status: ", winner)
    #print(tempList)
    #print(boardsInn)
    #result = 0
    #return result

f = open ("boards.txt", "r")
boardsList = f.readlines()

trimmedList = []
for element in boardsList:
    if element > "": # Fungerer ikke?
        trimmedList.append(element.strip())
#trimmedList = filter(None, boardsList)
#print(boardsList)
#print(trimmedList)
winnerFound = False

polled = open ("polled.txt", "r")
polledList = polled.readline().split(",")

i = 5 # Starts with a list of the first five polled numbers.
while i < len(polledList):
    if winnerFound == False:
        #print (polledList[0:i])
        check_tables(polledList[0:i], trimmedList)
    i += 1

#print(boardsList)