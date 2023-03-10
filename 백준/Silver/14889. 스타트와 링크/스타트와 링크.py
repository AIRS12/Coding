N = int(input())
visited = [False for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
minimum = 1e9

def solutions(cnt, index):
    global minimum
    if cnt == N//2:
        start, link = 0, 0
        
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]

        minimum = min(minimum, abs(start - link))
        return
    
    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            solutions(cnt+1, i+1)
            visited[i] = False
    
solutions(0,0)
print(minimum)