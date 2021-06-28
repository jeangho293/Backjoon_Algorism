# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/2606
   
   난이도 : __실버 3__
   
##요점 
  - `graph`를 구현하여 연결된 노드들을 파악하는 문제
   
  - `DFS` 또는 `BFS`를 활용하면 쉽게 풀 수 있는 문제다.

## 풀이
1. __graph__를 구상한다. 양방향을 가진 간선이라는 점을 주의.
    ```
    for _ in range(int(sys.stdin.readline())):
        x, y = map(int, sys.stdin.readline().split())

        # 서로 연결되어 있다는 의미는 양방향 간선을 가진다는 의미이다.
        graph[x].append(y)
        graph[y].append(x)
   ```
2. `BFS` 알고리즘
    ```
    while queue:
    location = queue.popleft()
    for node in graph[location]:    # 현재 부모 노드와 연결된 자식 노드들
        if not visited[node]:       # 방문한적이 없는 노드일 경우
            visited[node] = True
            virus_computer += 1
            queue.append(node)
    ```
    - 그림으로 구분한다면,
    ![KakaoTalk_20210628_163519064](https://user-images.githubusercontent.com/84619866/123598003-02626f00-d82f-11eb-8065-391f57d74e14.jpg)
