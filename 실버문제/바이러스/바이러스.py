from collections import deque, defaultdict
import sys

graph = defaultdict(list)
computer = int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())

    # 서로 연결되어 있다는 의미는 양방향 간선을 가진다는 의미이다.
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (computer + 1)      # 첫번째 바이러스 컴퓨터는 1이므로 편하게 index를 구성하기위함
queue, visited[1] = deque([1]), True
virus_computer = 0      # 감영된 바이러스의 갯수
while queue:
    location = queue.popleft()
    for node in graph[location]:    # 현재 부모 노드와 연결된 자식 노드들
        if not visited[node]:       # 방문한적이 없는 노드일 경우
            visited[node] = True
            virus_computer += 1
            queue.append(node)
print(virus_computer)