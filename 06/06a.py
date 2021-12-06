innTxt = ""
l = []
days = 80

f = open ("input.txt", "r")
innTxt = f.readline()
l = innTxt.split(",")

j = 0
while j < days:
    i = 0
    while i < len(l):
        if l[i] == 0:
            l[i] = 6
            l.append(int(9)) #9 to make sure it's at 8 after the next run
        else:
            l[i] = int(l[i]) - 1 
        i += 1
    j += 1

print("Totalt: ", len(l))