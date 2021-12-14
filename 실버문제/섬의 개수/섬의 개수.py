import sys
from collections import deque

moving_xy = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 해당위치로부터 8가지 방향 (대각선포함)
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == m == 0:     # while문 탈출 조건
        break
    else:
        maps = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]     # 맵 구현
        visited = [[False] * n for _ in range(m)]   # 방문 기록 구현
        cnt = 0     # 섬의 갯수

        # 그래프의 갯수를 구하기위함이니 모든 좌표에 대해 탐색을 실시한다.
        for x in range(m):
            for y in range(n):
                if maps[x][y] and not visited[x][y]:
                    queue, visited[x][y] = deque([[x, y]]), True
                    cnt += 1

                    while queue:
                        _x, _y = queue.popleft()
                        for move in moving_xy:  # 대각선을 포함하는 모든 방향에 대해 경로 탐색
                            moved_x, moved_y = move[0] + _x, move[1] + _y
                            if 0 <= moved_x < m and 0 <= moved_y < n and maps[moved_x][moved_y] and not visited[moved_x][moved_y]:
                                visited[moved_x][moved_y] = True
                                queue.append([moved_x, moved_y])
    print(cnt)