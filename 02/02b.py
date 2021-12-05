forward = 0
depth = 0
aim = 0
movement = 0

f = open("input.txt", "r")
for line in f:
    innLinje = line.split()
    if innLinje[0] == 'forward':
        forward = forward + int(innLinje[1])
        depth = depth + (aim * int(innLinje[1]))
    elif innLinje[0] == 'up':
        aim = aim - int(innLinje[1])
    elif innLinje[0] == 'down':
        aim = aim + int(innLinje[1])
movement = forward * depth
print('Forward: ', forward)
print('Depth: ', depth)
print('Movement: ', movement)