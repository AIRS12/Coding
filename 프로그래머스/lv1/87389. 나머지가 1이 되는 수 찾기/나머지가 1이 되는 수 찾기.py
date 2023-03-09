def solution(n):
    for answer in range(2, n):
        if(n-1)%answer == 0:
            print(answer)
            return answer
