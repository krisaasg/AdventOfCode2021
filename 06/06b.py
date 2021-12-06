fish = [ [0]*2 for n in range(10) ]
sum = 0
days = 256

f = open ("input.txt", "r")
innList = f.readline().split(",")
for i in range(0, len(innList)):
        innList[i] = int(innList[i])
for element in innList:
    if element == 1:
        fish[1][0] += 1
    elif element == 2:
        fish[2][0] += 1
    elif element == 3:
        fish[3][0] += 1
    elif element == 4:
        fish[4][0] += 1
    elif element == 5:
        fish[5][0] += 1
    elif element == 6:
        fish[6][0] += 1

i = 0
while i < days:
    for j in range (0,10):
        fish[j][1] = fish[j][0]
    fish[8][0] = fish[0][1]
    fish[7][0] = fish[8][1]
    fish[6][0] = fish[7][1] + fish[0][1]
    fish[5][0] = fish[6][1]
    fish[4][0] = fish[5][1]
    fish[3][0] = fish[4][1]
    fish[2][0] = fish[3][1]
    fish[1][0] = fish[2][1]
    fish[0][0] = fish[1][1]
    i += 1

i = 0
while i < len(fish):
    sum = sum + fish[i][0]
    i += 1

print("Totalt: ", sum)