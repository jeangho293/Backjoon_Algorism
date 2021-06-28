from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]      # 미로 설정
moving_xy = [(0, 1), (0, -1), (-1, 0), (1, 0)]      # 상하좌우로 이동좌표
visited = [[False] * m for _ in range(n)]           # 지니온 경로인지를 파악하는 visited 리스트

queue = deque([[0, 0]])     # 첫시작은 (0, 0)의 좌표로 시작
visited[0][0] = True        # 첫시작은 이미 방문했다

while queue:
    x, y = queue.popleft()
    for move in moving_xy:
        moved_x, moved_y = x + move[0], y + move[1]     # 현재 위치에서 상하좌우로 갈 수 있는 경로 파악

        # 주어진 2차원 리스트의 범위 안, 아직 방문하지 않은 장소, 벽이 아닌 길인 장소에 대한 조건
        if 0 <= moved_x < n and 0 <= moved_y < m and maps[moved_x][moved_y] and not visited[moved_x][moved_y]:
            visited[moved_x][moved_y] = True
            maps[moved_x][moved_y] += maps[x][y]        # 여태 자나온 경로를 구한다.
            queue.append([moved_x, moved_y])

print(maps[-1][-1])