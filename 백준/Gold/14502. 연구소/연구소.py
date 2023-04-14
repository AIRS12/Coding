import copy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

#벽  3개 세우기
def build(wall):
    global result

    if wall == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = board[i][j]
                visited[i][j] = 0

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2 and visited[i][j] == 0:
                    visited[i][j] = 1
                    virus(i,j)       

        result = max(safe(), result)
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                build(wall + 1)
                board[i][j] = 0   

#바이러스 확산
def virus(x,y):
     for dir in range(4):
        next_x = x + dx[dir]
        next_y = y + dy[dir]
        if (0 <= next_x < N) and (0 <= next_y < M ) and temp[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
            temp[next_x][next_y] = 2
            visited[next_x][next_y] = 1
            virus(next_x, next_y)

def safe():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1

    return cnt

build(0)
print(result)