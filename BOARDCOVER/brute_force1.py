#input.txt는 redirection으로 처리

from itertools import product

#완전 탐색으로 해결
def boardcover(H, W, board):                                #편의를 위해 0과 1로 바꿈
    board2 = [[0] * W for _ in range(H)]
    for i, j in product(range(H), range(W)):
        board2[i][j] = [0,1][board[i][j] == '#']
    if sum([row.count(0) for row in board2]) % 3 != 0:      #흰 칸의 개수가 3의 배수여야 해결 가능
        return 0
    else:
        return cover(H,W,board2)

#아직 채우지 못한 칸 중 가장 윗줄 가장 왼쪽에 있는 칸 찾기
def find_white(H,W,board):
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                return i, j
    return -1, -1
    '''
    for i,j in product(range(H), range(W)):
        if board[i][j] == 0:
            return i, j
    return -1, -1
    '''

#주어진 칸을 덮을 수 있는 네가지 방법 (가장 처음으로 만나는 빈 칸)
#(dy, dx): 블록을 구성하는 세 칸의 상대적 위치
coverType = [
    [(0,0), (1,0), (0,1)],
    [(0,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1)],
    [(0,0), (1,0), (1,-1)],
]


#board 의 (y,x)를 type 유형으로 처리
#delta가 1이면 덮고, -1 이면 덮었던 블록 제거
#덮을 수 있으면 True, 덮을 수 없으면 False 반환
def place(board, y, x, type, delta, H, W):
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if not ((0 <= ny < H) and (0 <= nx < W)):           #보드 밖으로 나간 경우
            ok = False
        else:
            board[ny][nx] += delta                          #칸을 채우거나 제거
            if (board[ny][nx] > 1):                         #검은 칸이거나 겹쳐서 덮는 경우
                ok = False
    return ok




    
#board의 모든 빈 칸을 덮을 수 있는 방법의 수 반환
#board[i][j] == 1 : 덮인 칸 (black)    
#board[i][j] == 0 : 빈 칸 (white)
def cover(H,W,board):
    y,x = find_white(H,W,board)                             #비어있는 첫번째 칸 찾기
    if y == -1:
        return 1                                            #모든 칸이 채워졌으므로 1 반환
    else:
        ret = 0
        for type in range(4):                               #모든 블록 유형에 대해 시도
            if (place(board, y, x, type, 1, H, W)):
                ret += cover(H, W, board)                   #덮을 수 있다면 재귀호출
            place(board, y, x, type, -1, H, W)              #덮은 블록은 제거
        return ret

for _ in range(int(input())):
    H, W = map(int, input().split())                        #보드의 크기
    board = [input() for _ in range(H)]                     #보드의 상태
    print(boardcover(H, W, board))                          #흰 칸을 덮는 방법의 수
