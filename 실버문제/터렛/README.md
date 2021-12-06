# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1002

난이도 : __실버 4__

## 요점

- `원의 방정식`으로 풀어야한다. (원의 방정식 말고 또 있을려나..?)
- `외접, 내접, 겹칠 때, 아무것도 겹치지 않을 때`에 관한 케이스

## 풀이

```python
import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2:  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0) 
```

## 실행 결과

