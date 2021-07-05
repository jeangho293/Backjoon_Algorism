from collections import Counter
import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
number_counter = Counter(number_list)
stack, result = [], [-1] * n

for i, value in enumerate(number_list):
    while stack and number_counter[stack[-1][1]] < number_counter[value]:
        _i, _value = stack.pop()
        result[_i] = value
    stack.append([i,  value])

for i in result:
    print(i, end=' ')