# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/9461

난이도 : __실버 3__

## 요점

- `다이나믹 프로그래밍`알고리즘 문제

이 문제는 독특한 규칙을 가지고 있다. 문제에서 준대로 `T(n) = T(n-3) + T(n-2)` 라는 규칙을 지니고 있다.

또한, 케이스 100까지에 대해 전부 계산해놓음으로 **입력이 많아질 경우** 똑같은 작업을 하지않도록 방지. 

## 풀이


```python
import sys

n = int(sys.stdin.readline())
target_list = [int(sys.stdin.readline()) for _ in range(n)]
triangles = [1, 1, 1]   # default 값으로 정해주어야 하는 값

for i in range(3, 101):     # 최대 수가 100까지 이므로
    triangles.append(triangles[i - 2] + triangles[i - 3])   # 규칙성으로 보아 T(n) = T(n-2) + T(n-3) 이라는 것을 알 수 있다.

for target in target_list:
    print(triangles[target - 1])

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145661684-c89abc99-1936-4398-a5df-5d1d4f14041c.png)
