h, m = input().split(":")
rings = input()
h = int(h)
m = int(m)
rings = int(rings)


def newHour():
    global h, rings
    if h == 12:
        h = 1
    else:
        h = h + 1
    rings -= h


def newMin():
    global m, rings
    if m == 45:
        newHour()
        m = 0
    else:
        m = m + 15
        rings -= 1


if m != 0:
    if m <= 15:
        m = 15
        rings -= 1
    elif m <= 30:
        m = 30
        rings -= 1
    elif m <= 45:
        m = 45
        rings -= 1
    elif m > 45:
        m = 0
        newHour()
else:
    rings -= h

while rings > 0:
    newMin()

print(str(h).zfill(2) + ":" + str(m).zfill(2))
