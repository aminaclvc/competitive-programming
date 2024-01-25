n = int(input())
word = input()

wasNum = False
nums = []
x = ""

for char in word:
    if char.isnumeric():
        x = x + char
    else:
        if len(x) > 0:
            nums.append(int(x))
            x = ""
if len(x) > 0:
    nums.append(int(x))

print(max(nums))
