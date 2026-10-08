def trianglepath(y,x):
    global n, T
    if y == n - 1:
        return T[y][x]
    else:
        down = trianglepath(y + 1, x)
        right = trianglepath(y + 1, x + 1)
        return T[y][x] + max(down, right)

for _ in range(int (input())):
    n = int(input())
    T = [list(map(int, input().split())) for _ in range(n)]
    print(trianglepath(0,0))