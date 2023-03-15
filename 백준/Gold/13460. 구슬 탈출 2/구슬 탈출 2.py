from collections import deque

# . # 0 R B => 빈칸, 장애물, 구멍, 빨간구슬, 파란구슬
N, M = map(int, input().split())
arr = []
red_x, red_y = 0, 0
blue_x, blue_y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    arr.append(list(input().strip()))
    for j in range(len(arr[i])):
        if arr[i][j] == 'R':
            red_x, red_y = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue_x, blue_y = i, j
            arr[i][j] = '.'

def move(x, y, dx, dy):
    next_x, next_y = x, y
    moving = 0
    while True:
        if arr[next_x+dx][next_y+dy] != '#' and arr[next_x+dx][next_y+dy] != 'O':
            next_x += dx
            next_y += dy
            moving += 1
        else:
            break

    return next_x, next_y, moving


def bfs():
    q = deque()
    q.append((red_x, red_y, blue_x, blue_y, 0))
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count >= 10:
            break

        for k in range(4):
            next_rx, next_ry, Rmove = move(rx, ry, dx[k], dy[k])
            next_bx, next_by, Bmove = move(bx, by, dx[k], dy[k])

            if arr[next_bx+dx[k]][next_by+dy[k]] == 'O':
                continue

            if arr[next_rx+dx[k]][next_ry+dy[k]] == 'O':
                return (count+1)

            if next_rx == next_bx and next_ry == next_by:
                if Rmove > Bmove:
                    next_rx -= dx[k]
                    next_ry -= dy[k]
                else:
                    next_bx -= dx[k]
                    next_by -= dy[k]

            if next_rx == rx and next_ry == ry and next_bx == bx and next_by == by:
                continue

            q.append((next_rx, next_ry, next_bx, next_by, count+1))
    
    return -1

result = bfs()
print(result)