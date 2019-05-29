import sys
import collections

finput = sys.stdin.readline

N = int(finput())
board = [list(map(int ,finput().split())) for _ in range(N)]
answer = 0
qu = collections.deque()


def enqueue(i, j):
    if board[i][j]:
        qu.append(board[i][j])
        board[i][j] = 0


def merge(i, j, di, dj):
    while qu:
        x = qu.popleft()
        if board[i][j] == 0:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x*2
            i, j = i+di, j+dj
        else:
            i, j = i + di, j + dj
            board[i][j] = x


def move(k):
    if k == 0:
        for j in range(N):
            for i in range(N):
                enqueue(i,j)
            merge(0,j,1,0)
    elif k == 1:
        for i in range(N):
            for j in range(N-1,-1,-1):
                enqueue(i,j)
            merge(i,N-1,0,-1)
    elif k == 2:
        for j in range(N):
            for i in range(N-1, -1, -1):
                enqueue(i,j)
            merge(N-1,j,-1,0)
    else:
        for i in range(N):
            for j in range(N):
                enqueue(i,j)
            merge(i,0,0,1)


def solve(cnt):
    global answer, board

    if cnt == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    tmpBoard = [x[:] for x in board]
    for k in range(4):
        move(k)
        solve(cnt+1)
        board = [x[:] for x in tmpBoard]


solve(0)
print(answer)