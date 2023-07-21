from collections import deque

def solution(queue1, queue2):
    answer = 0
    length = len(queue1) * 4
    s1, s2 = sum(queue1), sum(queue2)
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if (s1 + s2) % 2 != 0:
        return -1
    
    while(1):
        if answer > length:
            return -1
        if s1 == s2:
            return answer
        elif s1 > s2:
            answer += 1
            q = q1.popleft()
            q2.append(q)
            s1 -= q
            s2 += q
        else:
            answer += 1
            q = q2.popleft()
            q1.append(q)
            s2 -= q
            s1 += q
        
    return answer