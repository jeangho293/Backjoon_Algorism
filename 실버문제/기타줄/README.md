# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1049
   
   난이도 : __실버 4__
   
##요점
- __그리드 알고리즘__ 문제
    1. 기타줄 6개 중 가장 저렴한 브랜드의 가격을 `best_6` 으로 선언
    2. 기타줄 1개 중 가장 저렴한 브랜드의 가격을 `best_1` 로 선언
    3. `best_6` 의 가격을 기타줄 1개당의 효울로 계산한다. ----> `best_6 / 6` 은 1개당의 가격 가성비
        - 만약 1개당의 가격 가성비가 `best_1` 쪽이 저렴하다면 모든 기타줄은 `best_1` 가격으로 구매하는 것이 __최소 가격__
        - 만약 1개당의 가격 가성비가 `best_6` 쪽이 저렴하다면 `n // 6` 의 몫만큼은 필수로 `best_6` 로 구매하고 `n % 6` 인 나머지의 갯수는 `(n % 6) * best_1` 와 `best_6` 비교
        
## 풀이
1. 각각의 기타줄 종류에 대해서 가장 저렴한 브랜드를 구한다.
    ```
    for _ in range(m):
        line_6, line_1 = map(int, sys.stdin.readline().split())
        best_6, best_1 = min(line_6, best_6), min(line_1, best_1)
    ```

2. 1개당의 효율이 `best_1` 이 가장 저렴하다면 모든 기타줄은 `best_1` 가격으로 구매한다.
    ```
    if best_6 / 6 >= best_1:
        print(n * best_1)
    ```

3. `else`의 경우 --> 1개당의 효율이 `best_6` 가 가장 저렴한 경우
    ```
    else:
        need_money = n // 6 * best_6            # n // 6 몫만큼 best_6 가격으로 구매하고 나머지에 대한 비교를 한다.
        if best_6 <= (n % 6) * best_1:          #  n % 6 개에 대하여 기타줄 6개 한세트를 사는 것과 기타줄 1개씩 사는 것을 비교한다.
            need_money += best_6
        else:
            need_money += (n % 6) * best_1
        print(need_money)
    ```