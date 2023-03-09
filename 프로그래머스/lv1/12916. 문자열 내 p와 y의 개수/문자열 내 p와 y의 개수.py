def solution(s):
    p_num, y_num = 0, 0
    for word in s:
        if(word == 'p' or word == 'P'):
            p_num += 1

        elif(word == 'y' or word == 'Y'):
            y_num += 1

    if(p_num != y_num):
        return False

    return True