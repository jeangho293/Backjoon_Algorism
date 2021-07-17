from itertools import combinations
import sys, math

for _ in range(int(sys.stdin.readline())):
    number = list(map(int, sys.stdin.readline().split()))
    number_combination = list(combinations(number[1:], 2))
    result = 0

    for a, b in number_combination:
        result += math.gcd(a, b)
    print(result)