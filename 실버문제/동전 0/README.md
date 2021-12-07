# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/11047
   
   난이도 : __실버 2__
   
##요점
- `그리드 알고리즘`을 활용한 문제 풀이
- `divmod`를 활용했다. 굳이 divmod를 사용하지않고 몫과 나머지 연산으로 가능한 문제.
- sort()를 하지 않은 이유는 연산시간을 아끼기 위해서였으며 애초에 입력자체가 오름차순이기에 **for문에서 역순으로 뽑아내면 되기때문**이다.


## 풀이

```python
import sys

n, money = map(int, sys.stdin.readline().split())
money_list = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0     # 총 동전의 갯수
for i in range(n - 1, -1, -1):
    q, money = divmod(money, money_list[i])     # divmod를 활용하여 몫과 나머지 전부 구함
    cnt += q
    if not money:   # 바꿔먹을 돈이 없으면 loof 문 탈출
        break
print(cnt)
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145034298-fa9a88a5-55a0-4205-86d6-43cd92a60cc6.png)