def solution(n, arr1, arr2):
    answer = []
    for i in range (0,n):
        enc = format(arr1[i] | arr2[i], 'b').zfill(n)
        enc = enc.replace('0',' ').replace('1','#')
        answer.append(enc)
        
    return answer