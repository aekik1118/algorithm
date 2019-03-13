import sys

fest2017Prize = ((500, 1), (300, 2), (200, 3), (50, 4), (30, 5), (10, 6))
fest2018Prize = ((512, 1), (256, 2), (128, 4), (64, 8), (32, 16))

fastinput = lambda: sys.stdin.readline().rstrip()

T = int(fastinput())

for _ in range(T):
    a, b = map(int, fastinput().split())
    result = 0
    totalRank = 0

    if a > 0:
        for p, i in fest2017Prize:
            totalRank += i
            if a <= totalRank:
                result += p
                break

    totalRank = 0

    if b > 0:
        for p, i in fest2018Prize:
            totalRank += i
            if b <= totalRank:
                result += p
                break

    print(result*10000)
