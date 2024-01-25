n = input()
max = 0
for i in range(int(n)):
    a, b = input().split()
    max += int(a)
    if max < int(b):
        print("impossible")
        exit()
print("possible")
