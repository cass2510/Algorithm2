MOD = 10000000


# n개의 정사각형으로 이루어졌고, 맨 위 가로줄에 first개의
# 정사각형을 포함하는 폴리오미노의 수를 반환한다.
def poly(n, first):
    if n == first:       # 첫 줄에 모두 다 놓으면
        return 1         # 경우의 수는 하나
    else:
        # 나머지로 만들 수 있는 경우의 수와
        # 합칠 수 있는 경우의 수의 곱을 모두 더한다.
        ret = 0

        for second in range(1, n - first + 1):
            ret = (
                ret
                + (second + first - 1)
                * poly(n - first, second)
            ) % MOD

        return ret


''' P.4.3. 폴리오미노 (ID: POLY): 분할 정복 '''

for _ in range(int(input())):
    n = int(input())  # 폴리오미노를 구성할 정사각형의 수

    ret = 0

    # 첫 줄에 놓을 수 있는 모든 경우의 수를 합한다.
    for i in range(1, n + 1):
        ret = (ret + poly(n, i)) % MOD

    print(ret)