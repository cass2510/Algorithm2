def trianglepath(y,x):
    global n, T, cache
    cache = [[-1] * (i + 1) for i in range(n)]
    if y == n - 1:
        return T[y][x]
    elif cache[y][x] != -1:
        return cache[y][x]
    else:
        down = trianglepath(y + 1, x)
        right = trianglepath(y + 1, x + 1)
        cache[y][x] = T[y][x] + max(down, right)
        return cache[y][x]

for _ in range(int (input())):
    n = int(input())
    T = [list(map(int, input().split())) for _ in range(n)]
    print(trianglepath(0,0))