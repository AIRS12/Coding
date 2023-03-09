def solution(price, money, count):
    answer = -1
    price_money = 0
    for i in range(count+1):
        price_money += price * i
        print(price_money)
        
    if(money < price_money):
        answer = price_money - money
    else:
        answer = 0

    return answer