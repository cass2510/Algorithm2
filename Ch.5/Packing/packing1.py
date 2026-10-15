def packing(i, include):
        global n, W, items, w, p, optval, optsol
        if i == n:
            weight = sum([w[j] for j in range(n) if include[j]])
            profit = sum([p[j] for j in range(n) if include[j]])
            if weight <= W and optval < profit:
                optval = profit
                optsol = include[:]
        else:
            include[i] = True
            packing(i + 1, include)
            include[i] = False
            packing(i + 1, include)

for _ in range(int(input())):
    n, W = map(int, input().split())    #아이템의 수, 배낭 무게
    items = [input().split() for _ in range(n)]     #아이템 집합
    w = [int(items[i][1]) for i in range(n)]        #아이템의 무게
    p = [int(items[i][2]) for i in range(n)]        #아이템의 가치
    optval = 0  #최적값
    optsol = [False] * n    #최적해
    packing(0, [False] * n) #0번째 아이템부터 완전 탐색
    print(optval, sum(optsol))
    print(*[items[i][0] for i in range(n) if optsol[i]], sep = "\n")