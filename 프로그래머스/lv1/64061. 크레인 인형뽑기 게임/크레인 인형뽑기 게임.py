def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0 :
                if len(stack) != 0 and stack[-1] == board[i][move-1] :
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(board[i][move-1])
                
                board[i][move-1] = 0
                break
                
    return answer
