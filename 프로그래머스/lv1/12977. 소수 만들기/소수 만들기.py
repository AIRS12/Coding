from itertools import combinations
def prime(arr):
    for i in range(2, arr//2 + 1):
        if arr % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if prime(sum(i)): 
            answer += 1
            
    print(answer)
    return answer