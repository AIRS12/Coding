def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계 & 3단계
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
    previous_char = ''
    
    for char in new_id:
        if char == '.' and previous_char == '.':
            continue
        if char not in allowed_chars:
            continue
            
        answer += char
        previous_char = char
    #4단계
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]

    #5단계
    if len(answer) == 0 :
        answer = 'a'
    #6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
    #7단계
    if len(answer) < 3:
        while len(answer) <= 2:
            answer += answer[-1]
        
    return answer