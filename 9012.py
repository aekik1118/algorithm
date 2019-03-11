import sys


def is_vps(x):
    stack = list()
    for i in x:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True

    return False


T = int(input())

for _ in range(T):
    ip = sys.stdin.readline().rstrip()

    if is_vps(ip):
        print("YES")
    else:
        print("NO")


