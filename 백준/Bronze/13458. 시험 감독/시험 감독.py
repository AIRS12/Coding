#시험감독

room = int(input())
people = list(map(int, input().split()))
num1, num2 = map(int,input().split())

cnt = room
for i in people:
    i -= num1
    if i > 0 :
        if i % num2 :
            cnt += (i//num2) + 1
        else:
            cnt += (i//num2)

print(cnt)