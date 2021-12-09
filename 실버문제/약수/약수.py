import sys

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
print(min(number) * max(number))
