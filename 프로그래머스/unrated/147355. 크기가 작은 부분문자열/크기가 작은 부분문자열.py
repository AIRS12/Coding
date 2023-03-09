def solution(t, p):
    answer = 0

    for word in range (len(t) - len(p) + 1):
        if(int(t[word:word + len(p)]) <= int(p)):
            answer += 1

    return answer