a, b = 0, 1

n = int(input())
for _ in range(n):
    b, a = a + b, b
print(b % 10007)