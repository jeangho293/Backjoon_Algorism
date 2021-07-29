import sys
from collections import Counter

n, k = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
stack = []

for target, i in Counter(number).most_common():
    for _ in range(i):
        stack.append(str(target))
print(' '.join(stack))