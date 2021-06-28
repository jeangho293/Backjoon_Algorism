# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/2178
   
   난이도 : __실버 1__
   
1. 요점
   - `마지막 도착지점까지 거쳐야하는 최소한의 칸 수` 를 구한다. 즉 최소한의 경로를 따지는 문제이므로 `BFS`문제 풀이법 적용.
   - `0`과 `1`로 이동가능한 칸인지를 판별
   
## 풀이

1. `maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]`

 - 간편하게 `미로의 크기`를 구현한다.
 
 2. `moving_xy = [(0, 1), (0, -1), (-1, 0), (1, 0)]`
  - 현재의 장소에서 `상하좌우`로 갈 수 있는 경로를 구한다.
  
  3. `if 0 <= moved_x < n and 0 <= moved_y < m and maps[moved_x][moved_y] and not visited[moved_x][moved_y]:`
   - 이동된 좌표 `moved_x`, `moved_y`가 조건에 해당 되었을 경우 동작한다.
