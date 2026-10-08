def fib1(n):
    global cache
    if n <= 1:
        return n
    elif cache[n] != -1:
        return cache[n]
    else:
        cache[n] = fib1(n - 1) + fib1(n - 2)
        return cache[n]


for _ in range(int(input())):
    n = int(input())
    result = (fib1(n + 1))
    print(result % 1000000007)