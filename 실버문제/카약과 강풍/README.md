# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/2891
   
   난이도 : __실버 5__ (그리드)
   
##요점
- `set()` 의 차집합을 활용하여 풀이한다.
- __그리드__ 알고리즘

## 풀이
1. `set()` 차집합을 활용하여 __카약을 잃어버린 팀이 여분을 가지고 있는 상황__ 에 대한 처리
    ```
    result_reserve = set(reserve) - set(lost)
    result_lost = set(lost) - set(reserve)
    ```
2. `in()` 을 활용하여 `result_reserve` 의 요소중 `(i + 1)` 과 `(i - 1)`이 `result_lost`에 있는지를 확인한다.
    ```
    for i in result_reserve:                # 여분을 가져온 팀으로부터 앞뒤로 잃어버린 팀이 있는지를 확인한다.
        if (i - 1) in result_lost:
            result_lost.remove(i - 1)
        elif (i + 1) in result_lost:
            result_lost.remove(i + 1)
      ```