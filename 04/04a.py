def check_tables(polledInn, boardsInn):
    # Sjkke om table vinner og i så fall kalkulere sum.
    winner = False
    i = 0
    while i < len(boardsInn) and winner == False:
        if winner == False:
            row = 0
            column = 0
            tempList = []
            for j in range(5):
                tempRow = boardsInn[(i+j)].split()
                tempList.append(tempRow)
            
            sumFound = 0
            sumUnmarked = 0
            
            while row < 5 and winner == False:
                column = 0
                sumFound = 0
                while column < 5 and winner == False:
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
            while column < 5 and winner == False:
                row = 0
                while row < 5 and winner == False:
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
    return(winner)

f = open ("boards.txt", "r")
boardsList = f.readlines()

trimmedList = []
for element in boardsList:
    if element > "": # Fungerer ikke?
        trimmedList.append(element.strip())

winnerFound = False

polled = open ("polled.txt", "r")
polledList = polled.readline().split(",")

i = 5 # Starts with a list of the first five polled numbers.
while i < len(polledList):
    if winnerFound == False:
        #print (polledList[0:i])
        winnerFound = check_tables(polledList[0:i], trimmedList)
        #print("Winner? ", winnerFound)
    i += 1