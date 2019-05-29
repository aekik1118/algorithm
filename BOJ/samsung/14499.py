import sys

finput = sys.stdin.readline

top, bottom, left, right, front, behind = [0]*6

N, M, y, x, K = map(int, finput().split())

board = [list(map(int ,finput().split())) for _ in range(N)]

command = list(map(int ,finput().split()))

dy, dx = (0,0,-1,1),(1,-1,0,0)


def solve():
    global y, x
    for i in command:
        y, x = move(y, x, i-1)


def move(y,x,com):

    global board, top, bottom, left, right, front, behind

    ny, nx = y+dy[com], x + dx[com]
    if ny<0 or nx<0 or ny >= N or nx >= M:
        return y, x

    rollDice(com)

    if board[ny][nx] == 0:
        board[ny][nx] = behind
    else:
        behind = board[ny][nx]
        board[ny][nx] = 0

    print(front)
    return ny, nx


def rollDice(com):
    global top, bottom, left, right, front, behind
    if com == 0:
        front, right, behind, left = left, front, right, behind
    elif com == 1:
        front, right, behind, left = right, behind, left, front
    elif com == 2:
        front, top, behind, bottom = bottom, front, top, behind
    else:
        front, top, behind, bottom = top, behind, bottom, front


solve()