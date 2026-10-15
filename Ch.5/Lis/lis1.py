def lis(n, A):
    if not A:
        return 0
    else:
        ret = 0
        for i in range(n):
            B = []
            for j in range(i + 1, n):
                if A[i] < A[j]:
                    B.append(A[j])
            ret = max(ret, 1 + lis(len(B), B))
        return ret

for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    print(lis(n,A))