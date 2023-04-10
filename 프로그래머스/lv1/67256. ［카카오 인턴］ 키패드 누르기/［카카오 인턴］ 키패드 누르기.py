def solution(numbers, hand):
    answer = ''
    
    keypad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    
    left = keypad['*'] 
    right = keypad['#']
        
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left = keypad[str(num)]
            
        elif num in [3,6,9]:
            answer += 'R'
            right = keypad[str(num)]
            
        else:
            l_distance = abs(left[0] - keypad[str(num)][0]) + abs(left[1] - keypad[str(num)][1])
            r_distance = abs(right[0] - keypad[str(num)][0]) + abs(right[1] - keypad[str(num)][1])
            
            if l_distance < r_distance :
                answer += 'L'
                left = keypad[str(num)]
            
            elif l_distance > r_distance :
                answer += 'R'
                right = keypad[str(num)]
            
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = keypad[str(num)]
                else :
                    answer += 'L'
                    left = keypad[str(num)]
            
    return answer