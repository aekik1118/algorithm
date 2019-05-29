import sys
import collections

finput = sys.stdin.readline

dq = collections.deque()
dq.append((0, 0))

N = int(finput())
K = int(finput())

board = [[0]*N for _ in range(N)]
board[0][0] = 1


for i in range(K):
    y, x = map(int, finput().split())
    board[y-1][x-1] = 2


L = int(finput())
info = [finput().split() for _ in range(L)]

dy, dx = (-1,0,1,0), (0,1,0,-1)

board[0][0] = 1


def move(cy,cx, d):
    global board

    ny, nx = cy + dy[d], cx + dx[d]

    if ny >= N or nx >= N or nx < 0 or ny < 0 or board[ny][nx] == 1:
        return True
    elif board[ny][nx] == 0:
        dq.append((ny,nx))
        board[ny][nx] = 1
        py, px = dq.popleft()
        board[py][px] = 0
    else:
        dq.append((ny, nx))
        board[ny][nx] = 1

    return False


def solve():
    result = 0
    curD = 1

    for i in info:
        sec = int(i[0])

        for _ in range(result, sec, 1):
            result += 1
            cy, cx = dq[len(dq)-1]

            if move(cy, cx, curD):
                return result
        if i[1] == 'D':
            curD = (curD + 1) % 4
        else:
            curD = (curD + 3) % 4

    cy, cx = dq[len(dq) - 1]
    result += 1
    while not move(cy,cx,curD):
        result += 1
        cy, cx = dq[len(dq) - 1]

    return result


print(solve())
