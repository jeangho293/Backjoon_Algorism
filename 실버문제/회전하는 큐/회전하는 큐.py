from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N + 1)])
target_list = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in target_list:
    if queue.index(i) > len(queue) // 2:    # 현재 queue를 기준으로 오른쪽 또는 왼쪽이 더 빠르게 뽑아낼 수 있는지를 판별
        while queue[0] != i:    # queue 의 0번이 나올 때 까지 반복
            queue.appendleft(queue.pop())
            cnt += 1    # 3번 동작
    else:
        while queue[0] != i:    # queue 의 0번이 나올 때 까지 반복
            queue.append(queue.popleft())
            cnt += 1    # 2번 동작
    queue.popleft()     # 1번 동작
print(cnt)
