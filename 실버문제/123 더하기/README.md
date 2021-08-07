# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/9095

난이도 : __실버 3__

## 요점

- __DP(동적 프로그래밍)__ 을 활용한 문제
    - n == 1 일 때, 1가지 방법
    - n == 2 일 때, 2가지 방법
    - n == 3 일 때, 4가지 방법
    - n == 4 일 때, 7가지 방법

  ---> 점화식 : `f(n-1) + f(n-2) + f(n-3)` 으로 표현된다

## 풀이

1. 함수 표현식 ---> 재귀함수를 활용하여 DP를 구현
   def one_two_three(n):
``` def one_two_three(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            return one_two_three(n - 1) + one_two_three(n - 2) + one_two_three(n - 3)
   ```
