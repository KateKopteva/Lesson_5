from random import randint
# n = 100
l = [1, 2, 3, 0, -2, 5, 6]
# l = [randint(-10, 10) for _ in range(n)]
print(l)
count = 0
for i in range(1, len(l)):
    flag = False
    if l[i-1] < l[i]:
        continue
    else:
        count += 1
        flag = True
print(count)

