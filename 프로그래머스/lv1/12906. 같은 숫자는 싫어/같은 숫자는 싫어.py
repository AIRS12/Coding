def solution(arr):
    answer = []
    now = 1000001
    for i in range(len(arr)):
        if not arr[i] == now:
            answer.append(arr[i])
            now = arr[i]

    return answer