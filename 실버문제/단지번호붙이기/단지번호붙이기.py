import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
moving_xy = [(1, 0), (-1, 0), (0, 1), (0, -1)]      # 상하좌우에 대한 좌표이동

result, result_len = 0, []
for x in range(n):
    for y in range(n):
        if maps[x][y]:      # 한번도 방문하지 않은 장소
            queue, path = deque([[x, y]]), []       # 방문한 칸 수를 저장하는 리스트
            maps[x][y] = 0
            result += 1

            while queue:
                path.append([queue[0]])
                _x, _y = queue.popleft()
                for move in moving_xy:
                    moved_x, moved_y = _x + move[0], _y + move[1]
                    if 0 <= moved_x < n and 0 <= moved_y < n and maps[moved_x][moved_y]:
                        maps[moved_x][moved_y] = 0
                        queue.append([moved_x, moved_y])
            result_len.append(len(path))            # 이 영역에서 방문했던 칸 수의 길이

print(result)
for i in sorted(result_len):
    print(i)