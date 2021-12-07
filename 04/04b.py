# Solution works, but is a mess...

winnerFound = False
def check_tables(polledInn, boardsInn):
    winner = False
    firstLoser = False
    save1points = 0
    save2points = 0
    toggle = 0
    points = 0
#
    x = len(polledList)
    while x > 0:
        if firstLoser == False:
            polledInn = polledInn[0:x]
            i = 0
            while i < len(boardsInn):
                if winner == False and firstLoser == False:
                    row = 0
                    column = 0
                    tempList = []
                    for j in range(5):
                        tempRow = boardsInn[(i+j)].split()
                        tempList.append(tempRow)
                    
                    sumFound = 0
                    sumUnmarked = 0
                    
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
                        sumFound = 0
                        row += 1

                    row = 0
                    column = 0
                    while column < 5:
                        row = 0
                        sumFound = 0
                        while row < 5:
                            if tempList[row][column] in polledInn:
                                sumFound += 1
                            row += 1
                            if sumFound == 5:
                                winner = True
                        sumFound = 0
                        column += 1

                    # Storing two sets of data, since this solution will identify the last board to not win
                    # and running through numbers in reverse order. The board we want is thus the previous 
                    # board checked.
                    if toggle == 0:
                        save1points = sumUnmarked
                        toggle = 1
                    else:
                        save2points = sumUnmarked
                        toggle = 0
                    
                    
                    if winner == False and firstLoser == False:
                        # Summere alle umerkede, gange med nummer som utløste seier (siste nummer i polledInn)
                        points = sumUnmarked * int(polledInn[-1])
                        firstLoser = True                       
                        winningNumber = int(polledList[len(polledInn)])                       
                        if toggle == 1:
                            sumUnmarked = save1points
                        else:
                            sumUnmarked = save2points
                        points = (sumUnmarked - int(winningNumber)) * int(winningNumber)
                        print(points)

                winner = False
                i += 6 # New board starts every 6 lines
        x -= 1

f = open ("boards.txt", "r")
boardsList = f.readlines()

trimmedList = []
for element in boardsList:
    if element > "": # Fungerer ikke?
        trimmedList.append(element.strip())

polled = open ("polled.txt", "r")
polledList = polled.readline().split(",")

check_tables(polledList, trimmedList)