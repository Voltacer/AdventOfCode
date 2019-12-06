import math

s = []
def get_fuel(fuel):
    global s
    res = (math.floor(int(fuel) / 3)) - 2
    if (res > 0):
        s.append(res)
        get_fuel(res)

f = open('input.txt', 'r')
for l in f:
    get_fuel(l)


print(sum(s))