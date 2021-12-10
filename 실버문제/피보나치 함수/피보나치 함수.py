import sys

n = int(sys.stdin.readline())
fibonacci = [[1, 0], [0, 1]]    # f(0)과 f(1)은 미리 지정해준다. 예외 케이스 이므로

# 최대 N은 40이니 f(40)가지에 대해 미리 f(0), f(1)의 호출 횟수를 미리 계산
for i in range(2, 41):
    fibonacci.append(
        [fibonacci[i - 2][0] + fibonacci[i - 1][0], fibonacci[i - 2][1] + fibonacci[i - 1][1]]
    )

# target은 f(target)으로 구하면 된다.
for _ in range(n):
    target = int(sys.stdin.readline())
    cnt_0, cnt_1 = fibonacci[target]
    print(cnt_0, cnt_1)
