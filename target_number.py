from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    n = len(numbers)

    # idx 0인 초기값 저장
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    # 큐가 빌 때까지 반복
    while queue:
        # 제일 앞에꺼 뽑음
        temp, idx = queue.popleft()
        # numbers의 갯수만큼 수행
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            # numbers의 갯수만큼 수행하고 나온 값이 target과 같다면 answer + 1 
            if temp == target:
                answer += 1

    return answer