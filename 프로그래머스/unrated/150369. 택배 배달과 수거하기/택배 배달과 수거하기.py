def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver, pickup = 0, 0
    
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0 or pickups[i] != 0:
            cnt = 0
            while (deliver < deliveries[i] or pickup < pickups[i]):
                cnt += 1
                deliver += cap
                pickup += cap
            
            deliver -= deliveries[i]
            pickup -= pickups[i]
            answer += ((i+1) * cnt * 2)
            
    return answer