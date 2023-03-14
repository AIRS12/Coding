def solution(N, stages):
    result = {}
    people = len(stages)
    for stage in range(1, N+1):
        if people != 0:
            result[stage] = stages.count(stage) / people
            people -= stages.count(stage)
        else:
            result[stage] = 0
            
    print(result)
    print(sorted(result, key=lambda x : result[x], reverse=True))
    return sorted(result, key=lambda x : result[x], reverse=True)