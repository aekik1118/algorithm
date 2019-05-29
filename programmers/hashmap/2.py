def solution(phone_book):
    answer = True

    check = {}

    for i in phone_book:
        check[i] = 1

    for i in phone_book:
        key = ''
        for j in i:
            key += j
            if key in check:
                if check[key] == 0:
                    return False
                else:
                    check[key] = 0

    return answer



p = ["113", "12340", "123440", "12345", "98346"]
print(solution(p))