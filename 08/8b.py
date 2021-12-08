segments = []*10
patterns = []*4
translation = [0]*10
sumOut = 0
f = open ("input.txt", "r")
for line in f:
    subString = line.split(" | ")
    patterns = subString[1].split()
    segments = subString[0].split()
    for i in range(0, len(patterns)):
        patterns[i] = "".join(sorted(patterns[i])) # Patterns (list), letters of each pattern sorted alphabetically
    for i in range(0, len(segments)):
        segments[i] = "".join(sorted(segments[i])) # Segments (list), letters of each segment sorted alphabetically
    
    for i in range(0, len(segments)):
        if len(segments[i]) == 2:           # 1
            translation[1] = segments[i]
        elif len(segments[i]) == 3:         # 7
            translation[7] = segments[i]
        elif len(segments[i]) == 4:         # 4
            translation[4] = segments[i]
        elif len(segments[i]) == 7:         # 8
            translation[8] = segments[i]
    
    for i in range(0, len(segments)): # Samme loop as over, to make sure the obvious numbers are done first.
        if len(segments[i]) == 5:        # 2, 3 or 5 -     2 felles med 1 -> 3
            #print("2,3,5")
            diff = 0
            for j in range (0, len(segments[i])):
                if segments[i][j] not in translation[1]:
                    diff += 1
            if diff == 3:   # 3 is the only number of 2,3,5 with 3 not in common with 1.
                translation[3] = segments[i]
            elif diff == 4:
                diff = 0
                for j in range (0, len(segments[i])):
                    if segments[i][j] not in translation[4]:
                        diff += 1
                if diff == 3: # 2
                    translation[2] = segments[i]
                else:
                    translation[5] = segments[i]
    for i in range(0, len(segments)):
        if len(segments[i]) == 6: # 0, 6 or 9
            diff = 0
            for j in range (0, len(segments[i])):
                if segments[i][j] not in translation[4]: # (0->4=3 6->4=3 9->4=2)
                    diff += 1
            if diff == 2:   # 9->4=2
                translation[9] = segments[i]
            else: # 0 or 6 -  (0->1=4, 6->1=5)
                diff = 0
                for j in range (0, len(segments[i])):
                    if segments[i][j] not in translation[1]:
                        diff += 1
                if diff == 4: # 0
                    translation[0] = segments[i]
                else:   # 6
                    translation[6] = segments[i]
    output = ""
    for i in range(0, len(patterns)):
        for j in range(0, len(translation)):
            if patterns[i] == translation[j]:              
                output = output + str(j)
    #print(output)
    sumOut = sumOut + int(output)
print("Output: ", sumOut)