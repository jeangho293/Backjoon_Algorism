# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1002

난이도 : __실버 4__

## 요점

- `queue`를 사용하여 문제 풀이
- 가장 중요한 포인트는 **뽑아야할 데이터가 왼쪽 또는 오른쪽, 어느쪽이 가깝냐**다.
    
    그 판단을 위해서 `if queue.index(i) > len(queue) // 2:`에서 작동한다.

## 풀이

```python
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

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144986430-6d84db65-002a-48b3-8d16-60ced410881f.png)
