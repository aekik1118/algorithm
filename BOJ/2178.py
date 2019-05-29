import sys
import collections

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

fastinput = lambda: sys.stdin.readline().rstrip()

N, M = map(int,fastinput().split())

maze = [[int(x) for x in fastinput()] for _ in range(N)]

qu = collections.deque()

qu.append((0,0))
result = 1

while qu:
    quSize = len(qu)
    result += 1

    for _ in range(quSize):
        cy, cx = qu.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny == N-1 and nx == M-1:
                print(result)
                exit(0)
            elif ny >= 0 and nx >= 0 and ny < N and nx < M and maze[ny][nx] == 1:
                maze[ny][nx] = 2
                qu.append((ny, nx))
