import sys

def prime_search():
    _prime = [False, False] + [True] *(1_000_001 - 2)

    for i in range(2, int(1_000_001 ** 0.5) + 1):
        if _prime[i]:
            for j in range(i * i, 1_000_001, i):
                _prime[j] = False

    return _prime


prime = prime_search()
for _ in range(int(sys.stdin.readline())):
    target = int(sys.stdin.readline())
    cnt = 0

    for i in range(2, target // 2 + 1):
        if prime[i] and prime[target - i]:
            cnt += 1
    print(cnt)