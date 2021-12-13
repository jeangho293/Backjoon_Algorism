# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/9184

난이도 : __실버 2__

## 요점

- `문제에서 주어진 재귀 함수를 활용`하지만 매번 재귀함수를 호출하는 거이 아닌 **이미 연산 경험이 있을 경우**에는 계산없이 전의 연산결과를 가져옴.

## 풀이


```python
import sys


# 문제에서 주어진 함수에 대해서 그대로 받아왔음. 무슨 의미인지를 모름...
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:  # 이미 해당 연산했으면 그냥 return 하면 됨
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return dp[a][b][c]


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]     # 20이 넘으면 w(20,20,20)을 뽑으니 최대 리스트 숫자는 20개
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145804047-c807b187-4c3c-4830-a54a-72ab58bf2b39.png)
