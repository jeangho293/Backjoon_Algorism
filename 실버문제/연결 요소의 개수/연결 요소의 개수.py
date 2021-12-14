from collections import deque, defaultdict
import sys

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [False] * (n + 1)

# 그래프 구현
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n + 1):   # n의 갯수만큼 for문
    if not visited[i]:  # 한번도 방문하지 않은 노드가 있을 경우, 그 노드를 기준으로 BFS 탐색
        cnt += 1    # 그 노드를 가장 위쪽의 부모노드로 가정하여 트리 구현
        queue, visited[i] = deque([i]), True
        # BFS 구현
        while queue:
            location = queue.popleft()
            for node in graph[location]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
print(cnt)
