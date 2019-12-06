f = open('input.txt', 'r')
data = f.readline()
data = data.split(',')
newData = data.copy()


def handle(manipul, x, y):
    manipul[1] = x
    manipul[2] = y

    for i in range(0, len(manipul)):
        manipul[i] = int(manipul[i])

    for i in range(0, len(manipul), 4):
        opcode = manipul[i]
        v1 = manipul[i + 1]
        v2 = manipul[i + 2]
        targetOffset = manipul[i + 3]

        if opcode == 1:
            manipul[targetOffset] = manipul[v1] + manipul[v2]
        if opcode == 2:
            manipul[targetOffset] = manipul[v1] * manipul[v2]
        if opcode == 99:
            break

    return manipul[0]


for x in range(0, 100):
    for y in range(0, 100):
        data[1] = x
        data[2] = y
        if handle(data.copy(), x, y) == 19690720:
            print('x{}, y{}'.format(x, y))
