M, N = map(int, input().split())

# 에라토스테네스의 체
def prime_search(N):
    _prime = [False, False] + [True] * (N - 1)  # 1은 소수가 아니므로 False
    for i in range(2, int(N ** 0.5) + 1):   # 제곱근까지의 범위로 지정하면 시간복잡도 줄일 수 있음
        if _prime[i]:
            for j in range(i * i, N + 1, i):
                _prime[j] = False   # i의 배수는 배수이므로 소수가 될 수 없다. 모두 False로 변환
    return _prime


prime = prime_search(N)
for i in range(M, N + 1):
    if prime[i]:    # True는 모두 소수
        print(i)
