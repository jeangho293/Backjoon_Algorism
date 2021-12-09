import sys


def factorial(n):   # 팩토리얼 공식
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    bridge = factorial(b) // (factorial(b - a) * factorial(a))  # 조합 문제
    print(bridge)
