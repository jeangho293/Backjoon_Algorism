from collections import deque

def color_blind(n, maps, visited, moving_xy):
    color = {'R': 1, 'G': 1, 'B': 2}
    _maps = [m[:] for m in maps]
    _visited = [v[:] for v in visited]
    cnt = 0

    for x in range(n):
        for y in range(n):
             if not _visited[x][y]:
                queue = deque([[x, y]])
                _visited[x][y] = True
                cnt += 1

                while queue:
                    _x, _y = queue.popleft()
                    for move in moving_xy:
                        moved_x, moved_y = _x + move[0], _y + move[1]
                        if 0 <= moved_x < n and 0 <= moved_y < n and not _visited[moved_x][moved_y] and color[_maps[moved_x][moved_y]] == color[_maps[_x][_y]]:
                            _visited[moved_x][moved_y] = True
                            queue.append([moved_x, moved_y])

    return cnt


def non_color_blind(n, maps, visited, moving_xy):
    color = {'R': 1, 'G': 3, 'B': 2}
    _maps = [m[:] for m in maps]
    _visited = [v[:] for v in visited]
    cnt = 0

    for x in range(n):
        for y in range(n):
            if not _visited[x][y]:
                queue = deque([[x, y]])
                _visited[x][y] = True
                cnt += 1

                while queue:
                    _x, _y = queue.popleft()
                    for move in moving_xy:
                        moved_x, moved_y = _x + move[0], _y + move[1]
                        if 0 <= moved_x < n and 0 <= moved_y < n and not _visited[moved_x][moved_y] and color[
                            _maps[moved_x][moved_y]] == color[_maps[_x][_y]]:
                            _visited[moved_x][moved_y] = True
                            queue.append([moved_x, moved_y])
    return cnt


n = int(input())
maps = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
moving_xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

print(non_color_blind(n, maps, visited, moving_xy), color_blind(n, maps, visited, moving_xy))