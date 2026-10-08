MOD = 1000000007

def mmult(A, B):
    N, K, M = len(A), len(A[0]), len(B[0])
    C = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j])) % MOD
    return C


def mpow(A, n):
    # A^0은 단위행렬
    if n == 0:
        return [[1, 0], [0, 1]]

    # A^(n // 2)을 한 번만 계산
    half = mpow(A, n // 2)

    # A^n = A^(n//2) × A^(n//2)
    result = mmult(half, half)

    # n이 홀수이면 A를 한 번 더 곱함
    if n % 2 == 1:
        result = mmult(result, A)

    return result


def tiling(n):
    if n <= 2:
        return n
    else:
        A = [[1, 1], [1, 0]]
        return mpow(A, n)[0][0]


for _ in range(int(input())):
    n = int(input())
    print(tiling(n))