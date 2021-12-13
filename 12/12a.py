fullPaths = 0
pathList = []
caveConnections = []

def traverse_caves (path, cave, smallVisited):
    smallCavesVisited = smallVisited
    path.append(cave)
    global fullPaths 
        
    if (path[-1]).islower():
        smallCavesVisited.append(path[-1])   

    for i in range (len(caveConnections)):

        #Finds which rooms current cave has connections to, ignores small rooms allready visited.
        if caveConnections[i][0] == path[-1] and not caveConnections[i][1] in smallCavesVisited:
            if caveConnections[i][1] == 'end':
                pathList.append(path)               
                fullPaths +=1
            elif caveConnections[i][1] != 'start':
                traverse_caves(list(path), str(caveConnections[i][1]), list(smallCavesVisited))

def main():
    path = []
    start = 'start'
    f = open("input.txt", "r")
    for line in f:
        caveConnections.append(line.strip().split("-"))
        innLine = line.strip().split("-")
        innLine.reverse()
        caveConnections.append(innLine) # Reversing paths, to be able to use caveConnections[0] as "from" and [1] as "to"

    traverse_caves(list(path), str(start), [])
    print("Result: ", fullPaths)

if __name__ == "__main__":
    main()