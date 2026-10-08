def fib2(n):
    dp = [0, 1]

    for _ in range(2, n + 1):
        dp.append((dp[-1] + dp[-2]))
    return dp[n]


for _ in range(int(input())):
    n = int(input())
    result = (fib2(n + 1))
    print(result % 1000000007)