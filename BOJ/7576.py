import sys
import collections

input = lambda: sys.stdin.readline().rstrip()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solve(n, m, box):
    qu = collections.deque()
    result = -1

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                qu.append((i, j))

    while qu:
        result += 1
        quLen = len(qu)

        for _ in range(quLen):
            cy,cx = qu.popleft()

            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if ny >= 0 and nx >= 0 and ny < n and nx < m and box[ny][nx] == 0:
                    box[ny][nx] = 1
                    qu.append((ny,nx))

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1

    return result


m, n = map(int, input().split())
box = [[int(x) for x in input().split()] for _ in range(n)]
print(solve(n, m, box))