# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/11726
   
   난이도 : __실버 3__
   
##요점
- 이 문제는 `피보나치의 수열` 의 특징을 갖는다.
- python 은 __swap__ 기능을 쉽게 구현할 수 있다.
## 풀이
1. python 의 swap 구현
    ```
    for _ in range(n):
        b, a = a + b, b
    ```
    - 다른 언어와 다르게 `temp` 라는 또 하나의 변수를 쓰지 않고 swap 이 가능하다