# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/4948
   
   난이도 : __실버 2__
   
##요점
- `에라토스테네스의 체`를 활용한 비교적 짧은 시간복잡도 내의 소수 구하기

## 풀이

```python
# 에라토스테네스의 체
def prime_search():
    n = 123456 * 2 + 1  # 최대 수는 123465 이므로 이를 기준으로 2 * n 까지의 모든 소수를 구한다.
    _prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if _prime[i]:
            for j in range(i * i, n, i):
                _prime[j] = False
    return _prime


prime = prime_search()  # 에라토스네테스의 체는 한번만 실행하면 된다.
while True:
    n = int(input())
    if n == 0:  # 입력값이 0일 경우, 탈출
        break
    prime_cnt = len([i for i in range(n + 1, 2 * n + 1) if prime[i]])   # 범위에서 소수만 뽑아낸다.
    print(prime_cnt)
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144782741-e71e01d6-f2ea-4e22-a3e6-c76d3bb32984.png)