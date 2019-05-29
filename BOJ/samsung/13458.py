import sys

finput = sys.stdin.readline

answer = 0

N = int(finput())
A = list(map(int, finput().split()))
B, C = map(int, finput().split())

for i in range(N):
    A[i] -= B

    if A[i] > 0:
        answer += A[i] // C
        if A[i] % C != 0:
            answer += 1

answer += N

print(answer)