def solution(cards1, cards2, goal):
    card1idx , card2idx = 0 , 0
    
    answer = "Yes"
    
    for word in goal:
        if len(cards1) > card1idx and cards1[card1idx] == word:
            card1idx += 1
        elif len(cards2) > card2idx and cards2[card2idx] == word:
            card2idx += 1
        else:
            answer = "No"
            break
            
    return answer