# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/9613
   
   난이도 : __실버 3__
   
##요점
- `math.gcd` 를 활용한 __최대 공약수__ 구하기
- `itertools.combination` 을 활용한 __조합__ 구하기

## 풀이
1. `number_combination = list(combinations(number[1:], 2))`
    - `number[0]` 의 요소는 숫자의 갯수이므로 `number[1:]`부터 시작해서 2개의 수를 순서상관없이 조합

2. 조합된 수의 __GCD__ 를 구해서 더해준다.
    ```
    for a, b in number_combination:
        result += math.gcd(a, b)
     ```