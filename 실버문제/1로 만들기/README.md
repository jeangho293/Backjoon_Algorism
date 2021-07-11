
# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1463
   
   난이도 : __실버 3__
   
##요점
- `다이나믹 프로그래밍` 의 __메로이제이션__ 기법
    ![KakaoTalk_20210708_174906738](https://user-images.githubusercontent.com/84619866/124892455-dc9a4e80-e014-11eb-9866-f8f56917415e.jpg)

- `set()` 을 활용하여 중복되는 수에 대한 연산을 줄인다.

## 풀이
1. `super_node = set([n])`
    - 맨 처음 시작되는 N을 기준으로 시작된다.
 
2. 목표인 `1`이 `super_node`에 존재하면 무한 루프를 탈출하고 `cnt`를 출력
    ```
     if 1 in super_node:    # 무한 루트 탈출
        print(cnt)
        break
       ```