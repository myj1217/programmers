from collections import deque

def solution(maps):
    answer = 0

    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque()
        queue.append((x, y))
        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 게임 맵을 벗어난 경우 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                # 벽인 경우 무시
                if maps[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        # 상대 진영까지의 최단 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]
    # BFS를 수행한 결과 출력
    answer = bfs(0, 0)
    # 상대 팀 진영에 도착할 수 없을 때 -1
    return -1 if answer == 1 else answer