def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if reserve[i] == lost[j]:
                lost.remove(j)
    
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if abs(reserve[i] - lost[j]) == 1:
                lost.remove(j)
    
    answer = n - len(lost)
    
    return answer