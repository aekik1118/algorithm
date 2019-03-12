import sys

dp0 = list()
dp0.append(1)
dp0.append(0)

dp1 = list()
dp1.append(0)
dp1.append(1)

for i in range(40):
    dp0.append(dp0[i] + dp0[i+1])
    dp1.append(dp1[i] + dp1[i + 1])

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp0[n],dp1[n])



