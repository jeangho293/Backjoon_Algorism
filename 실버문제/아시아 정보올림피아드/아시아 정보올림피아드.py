import sys
from collections import defaultdict

country, cnt = defaultdict(int), 0
stack = [list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
for i in sorted(stack, key=lambda x: -x[2]):
    if country[i[0]] < 2:
        country[i[0]] += 1
        cnt += 1
        print(i[0], i[1])
    if cnt == 3:
        break