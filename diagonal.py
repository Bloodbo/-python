n = int(input('n='))
for i in range(n):
    k1 = n + 1 + i
    k2 = n + 1 + i
    for j in range(k2 + 1):
        print('*' if j >= k1 else ' ', end='')
    print()