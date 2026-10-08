def trianglepath(n, T):
    dp = [[-1] * n for _ in range(2)]
    dp[(n - 1) % 2] = T[n - 1][:]

    for i in range(n - 2, - 1, - 1):
        for j in range(i + 1):
            dp[i % 2][j] = T[i][j] + max(dp[(i + 1) % 2][j], dp[(i + 1) % 2][j + 1])
    return dp[0][0]

for _ in range(int(input())):
    n = int(input())
    T = [list(map(int, input().split())) for _ in range(n)]
    print(trianglepath(n,T))