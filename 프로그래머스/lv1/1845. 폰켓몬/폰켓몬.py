def solution(nums):
    answer = len(set(nums))
    print(answer)
    num = int(len(nums)/2)
     
    if answer > num:
        return num
    else:
        return answer