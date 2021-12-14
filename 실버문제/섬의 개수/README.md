# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/4963
   
   난이도 : __실버 2__
   
##요점
- `BFS 알고리즘을 이용한 문제`풀이
- `moving_xy = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]`로 현재 위치에서 이동할 수 있는 **좌표 경로**

- 내 의견: graph를 생성할 시, `1`의 인덱스 위치를 기억했다가 2중 for문 없이 `1`인 인덱스에 대한 경우만 계산했다면 더 빨랐을 것이다.

## 풀이

```python
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
                        for move in moving_xy:
                            moved_x, moved_y = move[0] + _x, move[1] + _y
                            if 0 <= moved_x < m and 0 <= moved_y < n and maps[moved_x][moved_y] and not visited[moved_x][moved_y]:
                                visited[moved_x][moved_y] = True
                                queue.append([moved_x, moved_y])
    print(cnt)
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145944380-67fdcb0d-74a3-4903-bb8a-2bac301d7661.png)