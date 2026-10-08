def fib3(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


for _ in range(int(input())):
    n = int(input())
    result = (fib3(n + 1))
    print(result % 1000000007)