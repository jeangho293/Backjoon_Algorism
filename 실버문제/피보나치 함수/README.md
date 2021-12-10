# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1003

난이도 : __실버 3__

## 요점

- `DP 알고리즘`으로 이전에 도출한 값을 **저장하여 재활용하는 방법**의 문제 풀이

## 풀이

```python
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

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145511484-334511f3-d744-4015-b236-42e89a127998.png)
