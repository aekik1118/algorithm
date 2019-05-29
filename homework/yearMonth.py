days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isleap(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False


while True:
    yearMonth = int(input("년과달을 입력하세요 \nex) '2019년 3월' = 201903 :"))
    year = yearMonth // 100
    month = yearMonth % 100
    day = 0

    if month > 0 and month <= 12:
        if month == 2 and isleap(year):
            day = 29
        else:
            day = days[month]

    print(year, "년", month, "월의 날수는", day, "일")



