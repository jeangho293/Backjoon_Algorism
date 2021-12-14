# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/11051

난이도 : __실버 1__

## 요점

- `동적 계획법`풀이이며 규칙을 찾기 위해서는 **파스칼의 삼각형**의 구조를 봐야한다. (안보면 규칙 못찾겠더라..)

- 추가적으로 `import math 의 math.factorial이 있는데 매우.. 효율적인 계산이 된다.`

## 풀이

```python
"""
n! // (n-k)! * k!
동적 계획법으로 풀이
파스칼 삼각형
"""

import sys

n, k = map(int, sys.stdin.readline().split())
cache = [[0] for _ in range(n + 2)]     # 현재까지 진행한 cache를 저장하는 리스트

for i in range(2, n + 2):
    for j in range(1, i + 1):
        if j == 1 or j == i:    # 파스칼 삼각형에 따르면 맨 처음과 맨 마지막은 1이다.
            cache[i].append(1)
        else:
            cache[i].append(cache[i - 1][j - 1] + cache[i - 1][j])

print(cache[-1][k + 1] % 10007)

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/146014874-949aca31-ba05-4f9a-8498-76099eb8ec7d.png)
