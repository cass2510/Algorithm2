def lis(start):
    global n, S, cache
    if cache[start] != -1: # 이미 계산된 값이 있으면 재활용
        return cache[start]
    else:
        ret = 1 # 항상 S[start]는 존재하므로 길이는 최하 1
        for next in range(start + 1, n):
            if S[start] < S[next]:
                ret = max(ret, lis(next) + 1)
        cache[start] = ret # 결과값을 캐시에 저장
        return cache[start]

for _ in range(int(input())):
    n = int(input())
    S = list(map(int,input().split()))
    cache = [-1] * n
    print(max(lis(i) for i in range(n)))