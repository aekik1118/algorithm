def solution(clothes):
    answer = 1

    check = {}

    for i in clothes:
        if i[1] in check:
            check[i[1]] += 1
        else:
            check[i[1]] = 2

    for i in check.values():
        answer *= i

    return answer-1

c =	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(c))
