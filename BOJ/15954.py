import sys
import math
from decimal import *

fastinput = lambda: sys.stdin.readline().rstrip()

n, K = map(int, fastinput().split())

preference = list(map(int, fastinput().split()))


def distribute(m, list):
    result = 0

    for i in list:
        result += (i-m)**2
    return result/len(list)


resultCandidate = list()

for i in range(n-K+1):
    for j in range(n-K-i+2):
        tmp = preference[i:i + K + j]
        m = sum(tmp) / len(tmp)
        dis = distribute(m, tmp)
        resultCandidate.append(dis)

result = min(resultCandidate)

print(math.sqrt(result))