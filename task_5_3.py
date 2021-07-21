def get_sumdelit(n):
    return sum(i for i in range(1, n) if n % i == 0)

for i in range(200, 301):
    friend_num = get_sumdelit(i)
    if i == get_sumdelit(friend_num):
        print(i, friend_num)


















