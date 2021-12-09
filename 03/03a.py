data = [0] * 12
gamma = [0] * 12
epsilon = [0] * 12
sGamma = ""
sEpsilon = ""
nLines = 0
f = open ("input.txt", "r")
for line in f:
    nLines += 1
    i = 0
    while i < 12:
        if line[i] == "1":
            data[i] += 1
        i += 1

j = 0
while j < 12:
    if data[j] > (nLines/2):
        gamma[j] = 1
        epsilon[j] = 0
    else:
        gamma[j] = 0
        epsilon[j] = 1
    j += 1
print(gamma)
print(epsilon)
sGamma = ''.join([str(elem) for elem in gamma])
sEpsilon = ''.join([str(elem) for elem in epsilon])

print(int(sGamma, 2))
print(int(sEpsilon, 2))

print("Result: ", int(sGamma, 2)*int(sEpsilon, 2))