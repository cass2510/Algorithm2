def lis(start):
    global n, S, cache, next_idx

    if cache[start] != -1: # 이미 계산된 값이 있으면 재활용
        return cache[start]
    else:
        ret = 1 # 항상 S[start]는 존재하므로 길이는 최하 1
        for next in range(start + 1, n):
            if S[start] < S[next]:
                if lis(next) + 1 > ret:
                    ret = lis(next) + 1
                    next_idx[start] = next # 다음에 선택할 인덱스 저장

        cache[start] = ret # 결과값을 캐시에 저장
        return cache[start]


for _ in range(int(input())):
    n = int(input())
    S = list(map(int, input().split()))
    cache = [-1] * n
    next_idx = [-1] * n

    start = max(range(n), key=lis)
    print(cache[start])

    result = []
    while start != -1:
        result.append(S[start])
        start = next_idx[start]

    print(*result)
