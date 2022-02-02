def solution(n, lost, reserve):
    answer = 0
    
    # 여벌 체육복을 가져왔지만 도난당한 학생의 경우
    # 이후 반복문을 돌릴 때 매우 까다롭기 때문에
    # 사전에 제외함
    res = [r for r in reserve if r not in lost]
    los = [a for a in lost if a not in reserve]

    for i in res:
        left = i - 1
        right = i + 1
        if left in los:
            los.remove(left)
        elif right in los:
            los.remove(right)
    
    answer = n - len(los)
    
    return answer