import sys

mapx = []
gY = 0
gX = 0
sys.setrecursionlimit(1000000000)


def waterFall(y, x):
    locmap = mapx
    mapx[y][x] = "~"
    if y < len(mapx) - 1:
        if mapx[y + 1][x] == "O":
            waterFall(y + 1, x)
        else:
            if mapx[y + 1][x] != "~":

                if x > 0:
                    if mapx[y][x - 1] == "O":
                        if mapx[y][x - 1] != "~":
                            waterFall(y, x - 1)
                if x < len(mapx[0]) - 1:
                    if mapx[y][x + 1] == "O":
                        if mapx[y][x + 1] != "~":

                            waterFall(y, x + 1)


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    y = lst[0]
    x = lst[1]
    w = lst[2]
    lst = list(map(int, input().split()))

    for i in range(y):
        line = input()
        ymap = []
        for char in line:
            ymap.append(char)
        mapx.append(ymap)

    for water in lst:

        waterFall(0, water)
    for dd in range(y):
        for yy in mapx[dd]:
            print(yy, end="")
        print()
