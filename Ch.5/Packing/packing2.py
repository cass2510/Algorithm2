def packing(i, capacity):
        global n, W, items, w, p, optval, optsol
        if i == n or capacity <= 0:
            return 0
        elif cache[i][capacity] != -1:
            return cache[i][capacity]
        else:
            pick = packing(i + 1, capacity -w[i])
            drop = packing(i + 1, capacity)
            cache[i][capacity] = drop if capacity < w[i] else max(drop, p[i] + pick)
            return cache[i][capacity]
        
def reconstruct (i, c):
    global n, items, w
    if i == n:
        return []
    elif packing(i, c) == packing(i + 1, c):
        return reconstruct(i + 1, c)
    else:
        return [items[i][0]] + reconstruct(i + 1, c - w[i])

for _ in range(int(input())):
    n, W = map(int, input().split())    #아이템의 수, 배낭 무게
    items = [input().split() for _ in range(n)]     #아이템 집합
    w = [int(items[i][1]) for i in range(n)]        #아이템의 무게
    p = [int(items[i][2]) for i in range(n)]        #아이템의 가치
    cache = [[-1] * (W + 1) for _ in range(n + 1)]
    optval = packing(0, W)
    optsol = reconstruct(0, W)
    print(optval, len(optsol))
    print(*optsol, sep = "\n")