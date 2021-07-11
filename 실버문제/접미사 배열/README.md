# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/11656
   
   난이도 : __실버 4__
   
##요점
- `list comprehension` 을 활용한 간략한 풀이가 핵심
- `sorted(iterable)` 는 __오름차순__ 으로 정렬이 된다.
    - 파이썬은 문자열에 대해서도 `sorted`가 동작되는데 비교값은 `unicode`로 바꿨을 때의 상수값으로 __오름차순 정렬__ 이 된다.
    - __내림차순__ 의 경우에는 `sorted(iterable, reverse=True)`