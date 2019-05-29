itemPrice = int(input("물건값을 입력하시오: "))
payment = int(input("지불 금액을 입력하시오: "))

change = payment - itemPrice

if change < 0:
    print("지불 글액이 부족합니다")
    exit(1)

#가장 적은 갯수의 지폐와 동전으로 하기위해서는 가장 큰돈을 우선적으로 거슬러주면 된다
#이를 귀류법으로 증명해보면 가장 큰단위의 돈으로 먼저 거슬러주지 않았을때 최소 갯수로 거슬러 줬다고 가정하면
#거슬러준 지폐와 동전을 이용해 더 큰단위의 지폐나 동전으로 바꿀수 있어야한다. 그 이유는 거스름돈을 가장 큰단위의 돈으로 거슬러 주지 않았기 때문이다.
#하지만 이 경우에 더 큰단위의 지폐나 동전으로 바꾸면 거스름돈의 지폐와 동전이 갯수가 줄어듬으로 위의 가정에 모순이 생긴다. 따라서 가장 큰돈을 우선적으로 거슬러주면 최소 갯수로 거슬러 줄수있다.

n50000note = change//50000
change = change%50000

n10000note = change//10000
change = change%10000

n5000note = change//5000
change = change%5000

n1000note = change//1000
change = change%1000

n500coins = change//500
change = change%500

n100coins = change//100
change = change%100

n50coins = change//50
change = change%50

n10coins = change//10
change = change%10

n5coins = change//5
change = change%5

n1coins = change//1
change = change%1

print("5만원권 : ",n50000note, "개")
print("1만원권 : ",n10000note, "개")
print("5천원권 : ",n5000note, "개")
print("천원권 : ",n1000note, "개")
print("500원 : ",n500coins, "개")
print("100원 : ",n100coins, "개")
print("50원 : ",n50coins, "개")
print("10원 : ",n10coins, "개")
print("5원 : ",n5coins, "개")
print("1원 : ",n1coins, "개")