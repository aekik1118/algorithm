import sys

finput = sys.stdin.readline

N, M = map(int, finput().split())

board = [list(map(int, finput().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]

Tshape = []
Tshape.append(((0,0),(0,1),(1,1),(0,2)))
Tshape.append(((0,0),(1,1),(1,0),(2,0)))
Tshape.append(((1,0),(1,1),(0,1),(1,2)))
Tshape.append(((1,0),(1,1),(0,1),(2,1)))

dy, dx = (-1,0,1,0), (0,1,0,-1)

def solve():
    global check
    answer = 0
    for i in range(N):
        for j in range(M):
            check[i][j] = True
            answer = max(answer, dfs(i, j, 0))
            answer = max(answer, checkTShape(i,j))
            check[i][j] = False

    return answer


def checkTShape(y, x):
    res = 0
    for i in Tshape:
        sum = 0

        for ty, tx in i:
            flag = True
            ny, nx = y+ty, x+tx
            if ny >= 0 and nx >= 0 and ny < N and nx < M:
                sum += board[ny][nx]
            else:
                flag = False
                break
        if flag:
            res = max(res, sum)

    return res


def dfs(y, x, cnt):
    global check

    res = 0

    if cnt == 3:
        return board[y][x]

    for i in range(1,4,1):
        ny, nx = y + dy[i], x + dx[i]
        if ny >= 0 and nx >= 0 and ny < N and nx < M and not check[ny][nx]:
            check[ny][nx] = True
            res = max(res , dfs(ny, nx, cnt+1))
            check[ny][nx] = False

    check[y][x] = False
    return res + board[y][x]

print(solve())