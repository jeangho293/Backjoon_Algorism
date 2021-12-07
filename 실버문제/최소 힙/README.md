# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1927
   
   난이도 : __실버 1__
   
## 요점
- 파이썬에서는 `import heapq`을 활용하며 간단하게 `heap_list` 를 구현 

- `try - except`를 활용하여 `heap_list`가 비어있을 경우 `IndexError`에 대한 예외를 처리한다.

## 풀이
1. __try - except__ 를 활용한 예외 처리
    ```
        try:                                # try - except 을 활용하여 IndexError(비어있는 경우) 처리
            print(heappop(heap_list))       # 힙 출력
        except:
            print(0)
    ```
   
## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144953072-b4528a1c-ee83-44eb-a137-e071047f741f.png)
