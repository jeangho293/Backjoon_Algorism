# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/9421
   
   난이도 : __실버 1__
   
##요점
- `에라토스네테스의 체`를 활용한 소수 판별
- `while`문을 활용하여 상근수 확인
    - 한번 나왔던 수가 반복적으로 나오면 순환수가 되므로 `value in set()` 을 활용하여 __중복된 수__ 임을 확인한다.

## 풀이
1. `prime_search()` 함수는 __에라토스테네스의 체__ 함수를 표현하였다.

2. __상근수__ 를 확인하는 함수
    ```
    def check_number(number):
        check = set()                   # 체크변수로 중복된 수임을 확인하기 위한 set()
        p_list = list(str(number))
    
        while 1 not in check:           # while문을 탈출하는 조건 --> 최종적으로 result == 1 일경우이다.
            result = 0
            for i in p_list:            # 각 자릿수의 제곱의 총합을 구하는 로직
                result += int(i) ** 2
    
            if result in check:         # 중복된 수인지를 확인
                return False
            else:
                check.add(result)
                p_list = list(str(result))
    
        return True
     ```

3. `에라토스테네스의 체` 를 통해 구한 소수에 대해서 _상근수_ 를 판별한다.
    ```
    for p in prime:
        if check_number(p):
            print(p)
      ```