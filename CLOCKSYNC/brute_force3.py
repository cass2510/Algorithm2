#input은 redirection

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

'''
D = {i:[] for i in range(16)}
for i in range(10):
    for j in linked[i]:
        D[j].append(i)
for key in D:
    print(key, D[key], sep=": ")
'''

# sequence 찾기

'''
D = {i:(4 - clocks[j]) % 4 for i, j in zip([1, 4, 9], [11, 8, 13])}
for sw in D:
    for _ in range(D[sw]):
        push(clocks, sw)
'''
sequence = [
    (8, linked[4]),
    (11, linked[1]),
    (13, linked[9]),
    (6, linked[3]),
    (10, linked[2]),
    (7, linked[7]),
    (4, linked[8]),
    (1, linked[0]),
    (3, linked[6]),
    (0, linked[5]),
]

def aligned(clocks):
    return not any(clocks)

def push (clocks, switch, cnt):
    for clock in linked[switch]:
        clocks[clock] = (clocks[clock] + cnt) % 4

def clocksync(clocks):
    ret = 0
    for clock, linked_clock in sequence:
        cnt = (4 - clocks[clock]) % 4
        for other in linked_clock:
            clocks[other] = (clocks[other] + cnt) % 4
        ret += cnt
    return -1 if any(clocks) else ret
    
INF = 31
for _ in range(int(input())):
    clocks = [(int(x) // 3) % 4 for x in input().split()]
    mincnt = clocksync(clocks)
    print(mincnt if mincnt < INF else -1)
