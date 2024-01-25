items, persons = input().split()
items = int(items)
persons = int(persons)
lst = list(map(int, input().split()))


x = (persons * 2) - items
for l in range(x):
    lst.append(0)
lst = sorted(lst, reverse=True)

cnt = 1
big = []
small = []
for x in lst:
    if cnt > len(lst) / 2:
        small.append(x)
    else:
        big.append(x)

    cnt += 1
big = sorted(big, reverse=True)
small = sorted(small)
check = []
for i in range(persons):
    check.append(small[i] + big[i])
print(max(check))
