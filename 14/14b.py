steps = 40
fPairs = dict()
f = open("input.txt", "r")
lines = f.readlines()
template = lines[0].strip()

pairs = []
for i in range (2,len(lines)):
    pairs.append(lines[i].strip().split(" -> "))

def find_first_pairs(s):
    for pair in range (len(pairs)):
        checkPair = pairs[pair][0]
        index = 0
        while index < len(s):
            index = s.find(checkPair, index)
            if index == -1:
                break
            index += 1
            fPairs[checkPair] = fPairs.get(checkPair, 0) + 1
    return(fPairs)

def new_pairs(fPairs, steps):
    letterCountsTotal = dict()
    letterCounts = dict()
    newPairs = dict()
    for step in range (steps):
        print("Step", step+1)
        newPairs.clear()     
        for i in range (len(pairs)):           
            pair = pairs[i][0]
            if pair in fPairs:
                for j in range (fPairs.get(pair)):
                    a = pair[:1]
                    b = pair[1:]
                    c = pairs[i][1]

                    if step < steps -1:
                        newPairs[a+c] = newPairs.get(a+c, 0) + 1
                        newPairs[c+b] = newPairs.get(c+b, 0) + 1

                    if step < steps:
                        letterCounts[c] = letterCounts.get(c, 0) + 1
                        letterCountsTotal[c] = letterCountsTotal.get(c, 0) + 1

        if step < steps -1:
            fPairs.clear()
            fPairs = dict(newPairs)

    letters = count_letters(letterCountsTotal)
    return(letters)

def count_letters(innLetters):
    letters = dict()
    innL = [*innLetters]

    for i in range (len(innL)):
        a = innL[i]
        n = innLetters.get(a)
        letters[a] = letters.get(a, 0) + n

    for i in range (len(template)):
        a = template[i]
        letters[a] = letters.get(a, 0) + 1




    return(letters)



def main():
    global steps
    pairDict = find_first_pairs(template)
    fElements = new_pairs(pairDict, steps)

    allValues = fElements.values()
    maxValue = max(allValues)
    minValue = min(allValues)
    diff = maxValue - minValue

    print("Result:", diff)

if __name__ == "__main__":
    main()