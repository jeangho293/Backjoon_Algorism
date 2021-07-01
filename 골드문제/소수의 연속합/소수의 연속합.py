from collections import deque


def prime_search(n):
    prime = [True] * (n + 1)

    for i in range(2, int((n + 1) ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return deque([i for i in range(2, n + 1) if prime[i]])

target = int(input())
prime, queue = prime_search(target), deque()

prime_sum, cnt = 0, 0
while True:
    if not queue and not prime:
        break

    if not queue:
        queue.append(prime.popleft())
        prime_sum = queue[0]

    try:
        if prime_sum == target:
            prime_sum -= queue.popleft()
            cnt += 1
            print(queue)
        elif prime_sum > target:
            prime_sum -= queue.popleft()
        else:
            push = prime.popleft()
            prime_sum += push
            queue.append(push)
    except:
        break

print(cnt)