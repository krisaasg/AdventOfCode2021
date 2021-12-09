filename = 'input.txt'

# innPoint: List of (x-coord,y-coord,height) per lowPoint. innMap: Height map with 9s as border.
def find_pool_size (innPoint, innMap):
    poolCells = set() # Set for pool coordinates to avoid duplicates.
    pointList = [] # Temporary list of points to check out per pool.
    pointList.append(innPoint)

    j = 0
    while j < len(pointList):
        x = pointList[j][0]
        y = pointList[j][1]
        height = int(pointList[j][2])
        poolCells.add(str(x)+','+str(y))
        if int(innMap[x+1][y]) > height and int(innMap[x+1][y]) < 9:
            newPoint = [x+1,y, int(innMap[x+1][y])]
            pointList.append(newPoint)
        if int(innMap[x-1][y]) > height and int(innMap[x-1][y]) < 9:
            newPoint = [x-1,y, int(innMap[x-1][y])]
            pointList.append(newPoint)
        if int(innMap[x][y+1]) > height and int(innMap[x][y+1]) < 9:
            newPoint = [x,y+1, int(innMap[x][y+1])]
            pointList.append(newPoint)
        if int(innMap[x][y-1]) > height and int(innMap[x][y-1]) < 9:
            newPoint = [x,y-1, int(innMap[x][y-1])]
            pointList.append(newPoint)
        j += 1
    return(len(poolCells))

# Creates a list (lines) of the input strings and trims away linebreak, returns formatted list.
def create_list(listSource):
    lines = []    
    f = open(listSource, "r")
    for line in f:
        lines.append('9' + line.strip() + '9')  # 
    lines.insert(0, "9"*len(lines[0]))          # Adds a frame of 9s around real data.
    lines.append("9"*len(lines[0]))             #
    return(lines)

# Formatted list with 9s is taken as input. Returns list with coordinates of lowpoints found.
def find_lowpoints(listInn):
    lines = listInn
    result = 0
    lowPoints = []
    # (1, len(x)-1) ignores frame of 9s
    for i in range (1,len(lines)-1):
        for j in range (1, len(lines[0])-1):
            checked = lines[i][j]
            if checked < lines[i-1][j] and checked < lines[i+1][j] and checked < lines[i][j+1] and checked < lines[i][j-1]:
                result = result + int(checked) + 1
                lowPoints.append([i,j,int(checked)]) # lowPoint as (x-coordinate, y-coordinate, height)
    return(lowPoints)

def main():
    poolSize = [] # For holding all pool sizes
    heightMap = create_list(filename)
    lowPoints = find_lowpoints(heightMap)
    for i in range(len(lowPoints)):
        poolSize.append(find_pool_size(lowPoints[i], heightMap))
    
    poolSize.sort(reverse=True)
    result = poolSize[0] * poolSize[1] * poolSize[2]

    print("Result: ", result)

if __name__ == "__main__":
    main()