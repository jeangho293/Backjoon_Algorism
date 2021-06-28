# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/11286
   
   난이도 : __실버 1__
   
##요점
1. `절댓값 abs(number)`를 통한 구현

2. `최소 힙, 최대 힙` 구현과 별반 다를 바가 없다.


## 풀이

1. `절댓값`을 활용하여 `heap_list`를 구성
    ```
     if not number:
        try:
            print(heappop(heap_list)[1])            # 원래의 수를 출력한다.
        except:
            print(0)
    else:
        heappush(heap_list, (abs(number), number))          
       ```