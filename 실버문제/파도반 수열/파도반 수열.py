import sys

n = int(sys.stdin.readline())
target_list = [int(sys.stdin.readline()) for _ in range(n)]
triangles = [1, 1, 1]   # default 값으로 정해주어야 하는 값

for i in range(3, 101):     # 최대 수가 100까지 이므로
    triangles.append(triangles[i - 2] + triangles[i - 3])   # 규칙성으로 보아 T(n) = T(n-2) + T(n-3) 이라는 것을 알 수 있다.

for target in target_list:
    print(triangles[target - 1])
