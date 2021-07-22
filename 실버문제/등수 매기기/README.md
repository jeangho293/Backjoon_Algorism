# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/2012
   
   난이도 : __실버 3__
   
##요점
- __그리디__ 문제
- 예상된 등수를 __오름차순__ 으로 정렬하고 정렬된 예상된 등수와 `rank`의 __절댓값 차__ 를 구한 후 모두 더한다.


## 풀이
1. 예상되는 등수 __오름차순__ 정렬

    `expect_rank = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])`
    
2. 정상적인 `rank` 를 리스트로 선언

    `rank = [i for i in range(1, len(expect_rank) + 1)]`

3. 예상되는 등수와 rank 를 빼고 절댓값 처리
    ```
    for expect, _rank in zip(rank, expect_rank):
        result += abs(expect - _rank)
    ```