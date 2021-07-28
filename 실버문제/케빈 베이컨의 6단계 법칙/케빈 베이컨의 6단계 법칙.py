from collections import deque, defaultdict

people, relation = map(int, input().split())
graph = defaultdict(list)
result = [[0, i] for i in range(people + 1)]

# 그래프 구현
for _ in range(relation):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, people + 1):
    visited = [False] * (people + 1)
    start, cnt = i, 1
    visited[i] = True
    queue = deque([i])

    while queue:
        sub_node = deque()
        while queue:
            location = queue.popleft()
            for node in graph[location]:
                if not visited[node]:
                    visited[node] = True
                    sub_node.append(node)
        queue = sub_node
        result[i][0] += len(sub_node) * cnt
        cnt += 1

print(sorted(result[1:])[0][1])