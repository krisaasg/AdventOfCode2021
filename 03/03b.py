def shorten_list(innList, filterBit, bitPlace):
    newList = []
    for item in innList:
        if item[bitPlace] == filterBit:
            newList.append(item.rstrip())
    return(newList)

n1 = 0

f = open ("input.txt", "r")
listInn = f.readlines()
listA = listInn
listB = listInn
print(listA)
i = 0
while len(listA) > 1:
    n1 = 0
    for item in listA:
        if item[i] == "1":
            n1 += 1
        
    if n1 >= (len(listA)/2):
        commonBit = "1"
    else:
        commonBit = "0"
    listA = shorten_list(listA, commonBit, i)
    i += 1

slistA = ''.join([str(elem) for elem in listA])
oxygen = int(slistA, 2)
print(slistA)
print(oxygen)


i = 0
while len(listB) > 1:
    n1 = 0
    for item in listB:
        if item[i] == "1":
            n1 += 1
        
    if n1 >= (len(listB)/2):
        uncommonBit = "0"
    else:
        uncommonBit = "1"
    listB = shorten_list(listB, uncommonBit, i)
    i += 1

slistB = ''.join([str(elem) for elem in listB])
co2 = int(slistB, 2)
print(slistB)
print(co2)

print("Result: ", oxygen*co2)   