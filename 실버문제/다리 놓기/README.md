# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1010
   
   난이도 : __실버 5__
   
##요점
- `순열 문제`이며 이항 계수를 통해 풀 수 있다. nCm
    - `n! // (n-m)! * (m)!`의 공식으로 풀이


## 풀이

```python
import sys


def factorial(n):   # 팩토리얼 공식
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    bridge = factorial(b) // (factorial(b - a) * factorial(a))  # 조합 문제
    print(bridge)

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145409886-f9b9a841-4964-4932-89eb-754856fec517.png)
