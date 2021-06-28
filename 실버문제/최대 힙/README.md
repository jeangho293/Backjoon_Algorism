# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/11279
   
   난이도 : __실버 2__
   
##요점
1. `최소 힙`을 활용하여 `최대 힙`을 구현한다.
    - `number`에 음수를 붙인다면, __최솟값은 최대값, 최솟값은 최대값__ 으로 역전이 된다.

## 풀이
1. `음수`를 활용한 `최대 힙 구현`
    ```
    if not number:
        try:
            print(-heappop(heap_list))      # heappop이 다시 -를 통해 원래 수로 바꾼다.
        except:
            print(0)
    else:
        heappush(heap_list, -number)        # 음수의 형태로 heappush
     ```