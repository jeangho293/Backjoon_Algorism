import sys

n = int(sys.stdin.readline())
number = sorted(list(map(int, sys.stdin.readline().split())))
target = int(sys.stdin.readline())

left, right = 0, len(number) - 1
cnt = 0
while left < right:
    two_sum = number[left] + number[right]
    if two_sum > target:
        right -= 1
    elif two_sum < target:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)