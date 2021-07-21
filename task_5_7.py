from random import randint
n = 4
m = 4
res_l = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(randint(1,9))
    res_l.append(l)
print(res_l)
for i in range (len(res_l)):
    maxx = max(res_l[i])
    res_l[i][i]=maxx
print(res_l)