def solution(n, words):
    answer = []
    dict = []
    for i, word in enumerate(words):
        if i == 0:
            dict.append(word)
            continue
            
        people = (i+1) % n #if people == 0: people = n
        if people == 0: people = n
        turn = ((i+1) + (n-1)) // n
        start = word[0]
        end = words[i-1][-1]
        if start == end:
            if word not in dict:
                dict.append(word)
                continue
            else:
                answer.extend([people, turn])
                break
        else:
            answer.extend([people, turn])
            break
    if not answer:
        answer.extend([0,0])
        
    return answer