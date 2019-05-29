import sys
import collections

input = sys.stdin.readline

N, M = map(int ,input().split())
board = [list(input().strip()) for _ in range(N)]
dy, dx = (-1,0,1,0), (0,1,0,-1)
qu = collections.deque()
check = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]


def init():

    rx,ry,bx,by = [0]*4

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                ry, rx = i,j
            elif board[i][j] == 'B':
                by, bx = i,j
    check[ry][rx][by][bx] = True
    qu.append((ry,rx,by,bx,0))


def move(y,x,di):
    c = 0
    while board[y][x] != 'O' and board[y+dy[di]][x+dx[di]] != '#':
        y += dy[di]
        x += dx[di]
        c += 1
    return y,x,c


def bfs():
    while qu:
        ry,rx,by,bx,d = qu.popleft()

        if d >= 10:
            break

        for i in range(4):
            nry, nrx, rc = move(ry,rx,i)
            nby, nbx, bc = move(by,bx,i)

            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                print(d+1)
                return
            if nry == nby and nrx == nbx:
                if rc > bc:
                    nry, nrx = nry - dy[i], nrx - dx[i]
                else:
                    nby, nbx = nby - dy[i], nbx - dx[i]

            if not check[nry][nrx][nby][nbx]:
                check[nry][nrx][nby][nbx] = True
                qu.append((nry,nrx,nby,nbx,d+1))

    print(-1)

init()
bfs()