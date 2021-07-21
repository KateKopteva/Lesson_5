num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
maxi = max(num)
for i in range(len(num)):
    if i % 2 == 0:
        num[i] = maxi
print(num)