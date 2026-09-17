import sys
sys.stdin = open("input.txt", "r", encoding ="utf-8")

linked = {
    0: [0,1,2],
    1: [3,7,9,11],
    2: [4,10,14,15],
    3: [0,4,5,6,7],
    4: [6,7,8,10,12],
    5: [0,2,14,15],
    6: [3,14,15],
    7: [4,5,7,14,15],
    8: [1,2,3,4,5],
    9: [3,4,5,9,13]
}

def aligned(clocks):
    return not any(clocks)

def push (clocks, switch):
    for clock in linked[switch]:
        clocks[clock] = (clocks[clock] + 1) % 4
        
def clocksync(clocks):
    ret = INF
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        for f in range(4):
                            for g in range(4):
                                for h in range(4):
                                    for i in range(4):
                                        for j in range(4):
                                            if aligned(clocks):
                                                cnt = a + b + c + d + e + f + g + h + i + j
                                                ret = min(ret, cnt)
                                            push(clocks, 9)
                                        push(clocks, 8)
                                    push(clocks, 7)
                                push(clocks, 6)
                            push(clocks, 5)
                        push(clocks, 4)
                    push(clocks, 3)
                push(clocks, 2)
            push(clocks, 1)
        push(clocks, 0)
    return ret

INF = 31
for _ in range(int(input())):
    clocks = [(int(x) // 3) % 4 for x in input().split()]
    mincnt = clocksync(clocks)
    print(mincnt if mincnt < INF else -1)
