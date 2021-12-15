steps = 10

f = open("input.txt", "r")
lines = f.readlines()
template = lines[0].strip()

pairs = []
for i in range (2,len(lines)):
    pairs.append(lines[i].strip().split(" -> "))

for step in range (steps):
    print("Step", step+1)
    changeQueue = []
    iDelta = 0 # String index delta, compensates for adding lengt the string when adding a letter.
    for pair in range (len(pairs)):
        
        checkPair = pairs[pair][0]
        newLetter = pairs[pair][1]
        index = 0
        while index < len(template):
            index = template.find(checkPair, index)
            if index == -1:
                break
            index += 1
            changeQueue.append([index,newLetter])
    changeQueue.sort()
    # Creating new template
    for change in range (len(changeQueue)):      
        letter = changeQueue[change][1]
        split = changeQueue[change][0] + iDelta
        template = template[:split] + letter + template[split:]
        iDelta += 1
print(len(template))

fElements = dict()
for i in range (len(template)):
    fElements[template[i]] = fElements.get(template[i], 0) + 1

allValues = fElements.values()
maxValue = max(allValues)
minValue = min(allValues)
diff = maxValue - minValue

print("Result:", diff)