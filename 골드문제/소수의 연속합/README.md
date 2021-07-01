# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1644
   
   난이도 : __골드 3__
   
##요점
- __에라토스테네스의 체__ 를 활용한 소수 판별
- `queue`를 활용하여 연속합을 구함.
- `투 포인트`를 활용하여 풀 수도 있었음. (시간은 비슷하게 걸림)
## 풀이
1. `while문을 벗어나기 위한 조건`으로 `prime`과 `queue`가 동시에 비어 있을 경우에만 탈출
    ```
    if not queue and not prime:
        break
      ```
    - 동시에 만족해야 하는 이유는 `prime`이 비었지만 `queue` 안에서 `popleft()`연산을 하다가 연속합이 만족될 경우도 존재.
        - 이 문제에서 대표적인 예로 `n = 41`일 때, `prime`은 비어있지만 `queue`에서 `[13, 17, 41]`이 존재하고 `popleft()`연산 후 `[41]`만 남을 경우 __조건 만족__
        
 2. 연속되는 소수의 합을 구하는 로직
    ```
    try:
        if prime_sum == target:             # 조건을 만족할 때
            prime_sum -= queue.popleft()    
            cnt += 1
        elif prime_sum > target:
            prime_sum -= queue.popleft()
        else:
            push = prime.popleft()
            prime_sum += push
            queue.append(push)
    except:                                 # break가 실행될 때는 더 이상 n을 만들수 없을 때
        break
       ```