sum = 0
innList = []
fuel = 0

f = open ("input.txt", "r")
innTxt = f.readline()
innList = innTxt.split(",")
for i in range(0, len(innList)):
        innList[i] = int(innList[i])
sumLow = int(max(innList)) * len(innList) # Worst case, for camparison

for i in range(0, max(innList)):
    for j in range(0, len(innList)):
        fuelCost = abs((innList[j] - i))
        fuel = fuel + fuelCost
    if fuel < sumLow:
        #print("New low: ", fuel)
        sumLow = fuel
    #print(i," - ", fuel)
    fuel = 0

print(sumLow)