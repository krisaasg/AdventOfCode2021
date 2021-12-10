sum = 0
innList = []
fuel = 0
sumLow = -1

f = open ("input.txt", "r")
innTxt = f.readline()
innList = innTxt.split(",")
for i in range(0, len(innList)):
        innList[i] = int(innList[i])

for i in range(0, max(innList)):
    for j in range(0, len(innList)):
        dist = abs((innList[j] - i))
        fuelCost = (dist*(dist+1))/2
        fuel = fuel + fuelCost
    if fuel < sumLow or sumLow < 1:
        sumLow = fuel
    fuel = 0

print(sumLow)