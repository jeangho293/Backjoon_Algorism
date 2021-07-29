n, m = map(int, input().split())

image = [list(map(int, input().split())) for _ in range(n)]
target = int(input())

cnt = 0
for x in range(n - 2):
    for y in range(m - 2):
        stack = []
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                stack.append(image[i][j])
        if sorted(stack)[4] >= target:
            cnt += 1
print(cnt)