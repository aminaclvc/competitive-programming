i = int(input())
lst = list(map(int, input().split()))

out = 0
for step in range(i):
    if step + 1 == i:
        while lst[step] != 1:
            lst[step] -= 1
            out += 1
    else:
        while lst[step] > lst[step + 1] + 1:
            lst[step] -= 1
            out += 1

print(out)
