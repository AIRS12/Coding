N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split())) # +, -, x, / 순서

maximum, minimum = -1e9, 1e9
#이 solution을 계속 돌리면서 계산 끝나면 max, min 리턴하고 끝

def solution(cnt, sum, plus, minus, multiple, divide):
    global maximum, minimum
    if cnt == N:
        maximum = max(sum, maximum)
        minimum = min(sum, minimum)
        return

    if plus:
        solution(cnt+1, sum+A[cnt], plus-1, minus, multiple, divide)
    if minus:
        solution(cnt+1, sum-A[cnt], plus, minus-1, multiple, divide)
    if multiple:
        solution(cnt+1, sum*A[cnt], plus, minus, multiple-1, divide)
    if divide:
        solution(cnt+1, int(sum/A[cnt]), plus, minus, multiple, divide-1)

solution(1, A[0], cal[0], cal[1], cal[2], cal[3] )

print(maximum)
print(minimum)