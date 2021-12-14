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
