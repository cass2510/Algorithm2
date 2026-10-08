MOD = 10000000


# 폴리오미노: 메모이제이션
# n개의 정사각형으로 이루어졌고, 맨 위 가로줄에 first개의
# 정사각형을 포함하는 폴리오미노의 수를 반환한다.
def poly(n, first):
    global cache

    # 모든 정사각형을 첫 줄에 놓는 경우
    if n == first:
        return 1

    # 이미 계산한 결과가 있으면 바로 반환
    elif cache[n][first] != -1:
        return cache[n][first]

    else:
        ret = 0

        # 두 번째 줄에 놓을 정사각형 수
        for second in range(1, n - first + 1):
            ret = (
                ret
                + (second + first - 1)
                * poly(n - first, second)
            ) % MOD

        # 계산한 결과를 캐시에 저장한다.
        cache[n][first] = ret

        return cache[n][first]

for _ in range(int(input())):
    n = int(input())  # 폴리오미노를 구성할 정사각형의 수

    # cache[i]는 인덱스 0부터 i까지 사용할 수 있다.
    cache = [[-1] * (i + 1) for i in range(n + 1)]

    ret = 0

    # 첫 줄에 놓을 수 있는 모든 경우의 수를 합한다.
    for i in range(1, n + 1):
        ret = (ret + poly(n, i)) % MOD

    print(ret)