def solution(lottos, win_nums):
    cnt = 0
    lotto = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    dontknow = lottos.count(0)
    
    for num in win_nums:
        if num in lottos:
            cnt += 1

    print(cnt) 
    return [ lotto[cnt+dontknow], lotto[cnt] ]