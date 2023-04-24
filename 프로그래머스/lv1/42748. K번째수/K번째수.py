def solution(array, commands):
    answer = []
    new_array = []
    for command in commands:
        i, j, k = command
        i = i - 1
        new_array = array[i:j]
        answer.append(sorted(new_array)[k-1])
        
    return answer