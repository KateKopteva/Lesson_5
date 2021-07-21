m, n = int(input()), int(input())
for i in range(m, n+1):
    d = []
    for j in range(2, i):
        if i % j == 0:
            d.append(j)
    print(str(i) + ':', *d)