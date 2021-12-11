squids = []
flashes = 0

def energy_increase():
    for i in range (len(squids)):
        for j in range (len(squids[i])):
            flash_squid(i,j)

def reset_squids():
    global flashes
    for i in range (len(squids)):
        for j in range (len(squids[i])):
            if squids[i][j] == 10:
                squids[i][j] = 0
        
def flash_squid (x,y):
    global flashes
    if squids[x][y] < 10:
        squids[x][y] += 1

        if squids[x][y] == 10:
            flashes += 1
            # Increment adjacent    
            if x != 0:
                if squids[x-1][y] < 10 : flash_squid(x-1,y)

            if x != len(squids[x])-1:
                if squids[x+1][y] < 10 : flash_squid(x+1,y)

            if y != 0:
                if squids[x][y-1] < 10 : flash_squid(x,y-1)

            if y != len(squids[y])-1:
                if squids[x][y+1] < 10 : flash_squid(x,y+1)

            # Diagonally
            if x != 0 and y != 0:
                if squids[x-1][y-1] < 10 : flash_squid(x-1,y-1)
            
            if x != 0 and y != len(squids[y])-1:
                if squids[x-1][y+1] < 10 : flash_squid(x-1,y+1)

            if x != len(squids[x])-1 and y != 0:
                if squids[x+1][y-1] < 10 : flash_squid(x+1,y-1)
            
            if x != len(squids[x])-1 and y != len(squids[y])-1:
                if squids[x+1][y+1] < 10 : flash_squid(x+1,y+1)

def all_flashing():
    flashing = 0
    for i in range (len(squids)):
        for j in range (len(squids[i])):
            if squids[i][j] == 10:
                flashing += 1
    if flashing == len(squids) * len(squids[0]):
        return(True)
    else:
        return(False)
             
def main():
    step = 0
    allFlash = False
    f = open("input.txt", "r")
    for line in f:
        lineList = []
        line = line.strip()
        for i in range (len(line)):
            lineList.append(int(line[i]))
        squids.append(lineList)

    #for i in range(steps):
    while allFlash == False:
        energy_increase()
        allFlash = all_flashing()
        reset_squids()
        step += 1
    print("All flashing first at ", step)

if __name__ == "__main__":
    main()