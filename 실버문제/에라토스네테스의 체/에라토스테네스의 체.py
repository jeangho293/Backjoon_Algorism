def Prime_Search(n, target):
    prime = [True] * (n + 1)
    cnt = 0

    for i in range(2, n + 1):
        if prime[i]:
            cnt += 1
            if cnt == target:
                return i
            for j in range(2 * i, n + 1, i):
                if prime[j] == True:
                    prime[j] = False
                    cnt += 1
                if cnt == target:
                    return j

n, target = map(int, input().split())
print(Prime_Search(n, target))