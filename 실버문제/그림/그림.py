from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
moving_xy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
total, result = 0, 0

for x in range(n):
    for y in range(m):
        if not visited[x][y] and maps[x][y] == 1:
            queue = deque([[x, y]])
            visited[x][y] = True
            cnt = 1
            total += 1

            while queue:
                _x, _y = queue.popleft()
                for move in moving_xy:
                    moved_x, moved_y = _x + move[0], _y + move[1]
                    if 0 <= moved_x < n and 0 <= moved_y < m and not visited[moved_x][moved_y] and maps[moved_x][moved_y] == 1:
                        queue.append([moved_x, moved_y])
                        visited[moved_x][moved_y] = True
                        cnt += 1
            result = max(result, cnt)
print(total)
print(result)