
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = []

buffer = {}
total = len(stages)

for i in range(1, N+1):
    if total != 0:
        cnt = stages.count(i)
        buffer[i] = cnt / total
        total -= cnt
    else:
        buffer[i] = 0

answer = sorted(buffer.items(),key=lambda x:x[1], reverse= True)
print(answer)

# def solution(N, stages):
#
#     answer = []
#
#     N = 5
#     stages = [2, 1, 2, 6, 2, 4, 3, 3]
#
#     visit = [int(0) for _ in range(N + 1)]
#     passCnt = [int(0) for _ in range(len(stages))]
#     buffer = []
#
#     stages.sort()
#     stages.reverse()
#
#     for i in stages:
#         if visit[i] == 0:
#            visit[i] = max(visit[i:]) + 1
#         else:
#             visit[i] += 1
#
#     tmp = 0
#
#     for i in reversed(range(N)):
#         if visit[i+1] == 0:
#             visit[i+1] = tmp
#         else:
#             tmp = visit[i+1]
#
#     for i in range(N):
#         rate = visit[i+1] / visit[i]
#         buffer.append((rate, i + 1))
#
#     buffer.sort(key=lambda element: element[0])
#
#     for i in buffer:
#         answer.append(i[1])
#
#     return answer

# visit배열 생성시 시간초과
# def solution(N, stages):
#     answer = []
#
#     visit = [0 for _ in range(N + 1)]
#     passCnt = [0 for _ in range(len(stages))]
#     buffer = []
#
#     for i in stages:
#         for j in range(i):
#             visit[j] += 1
#
#         for j in range(i - 1):
#             passCnt[j] += 1
#
#     for i in range(N):
#         rate = passCnt[i] / visit[i]
#         buffer.append((rate, i + 1))
#
#     buffer.sort(key=lambda element: element[0])
#
#     for i in buffer:
#         answer.append(i[1])
#
#     return answer


def solution(N, stages):
    buffer = {}
    total = len(stages)

    for i in range(1, N + 1):
        if total != 0:
            cnt = stages.count(i)
            buffer[i] = cnt / total
            total -= cnt
        else:
            buffer[i] = 0

    answer = sorted(buffer, key=lambda x: buffer[x], reverse=True)
    return answer