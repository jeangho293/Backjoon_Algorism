import sys

result = 0
expect_rank = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])
rank = [i for i in range(1, len(expect_rank) + 1)]

for expect, _rank in zip(rank, expect_rank):
    result += abs(expect - _rank)
print(result)