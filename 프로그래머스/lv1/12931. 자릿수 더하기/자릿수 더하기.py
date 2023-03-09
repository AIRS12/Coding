def solution(n):
    answer = 0
    n_list = list(map(int, str(n)))
    for num in range (len(n_list)):
        answer += n_list[num]

    return answer