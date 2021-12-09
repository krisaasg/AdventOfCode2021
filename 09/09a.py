result = 0

# Creates a list (lines) of the input strings and trims away linebreak
lines = []
f = open("input.txt", "r")
for line in f:
    lines.append('9' + line.strip() + '9')  # 
lines.insert(0, "9"*len(lines[0]))          # Adds a frame of 9s around real data
lines.append("9"*len(lines[0]))             #

# Iterates through data, ignoring frame of 9s
for i in range (1,len(lines)-1):
    for j in range (1, len(lines[0])-1):
        checked = lines[i][j]
        if checked < lines[i-1][j] and checked < lines[i+1][j] and checked < lines[i][j+1] and checked < lines[i][j-1]:
            result = result + int(checked) + 1
print("Result: ", result)