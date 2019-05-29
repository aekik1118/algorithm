def solution(participant, completion):
    answer = ''
    check = {}

    for i in completion:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1

    for i in participant:
        if i in check:
            if check[i] == 0:
                answer = i
                break
            else:
                check[i] -= 1
        else:
            answer = i
            break

    return answer


p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]

print(solution(p,c))