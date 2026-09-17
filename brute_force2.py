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

def push (clocks, switch, cnt):
    for clock in linked[switch]:
        clocks[clock] = (clocks[clock] + cnt) % 4
        
from itertools import product
def clocksync(clocks):
    ret = INF
    for prod in product (range(4), repeat = 10):
        pushed = clocks[:]
        for switch in range(10):
            push(pushed, switch, prod[switch])
        if aligned(pushed):
            ret = min(ret, sum(prod))
    return ret
    
INF = 31
for _ in range(int(input())):
    clocks = [(int(x) // 3) % 4 for x in input().split()]
    mincnt = clocksync(clocks)
    print(mincnt if mincnt < INF else -1)