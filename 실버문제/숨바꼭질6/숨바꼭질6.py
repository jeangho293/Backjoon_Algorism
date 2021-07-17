from math import gcd
import sys

N, S = map(int, sys.stdin.readline().split())
brother = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    brother[i] = abs(S - brother[i])

for i in range(1, N):
    brother[i] = gcd(brother[i - 1], brother[i])
print(brother[-1])