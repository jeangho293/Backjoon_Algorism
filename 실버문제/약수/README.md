# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/1037
   
   난이도 : __실버 5__
   
##요점

- `최댓값` 과 `최솟값`을 곱하면 원래의 수가 나온다.

## 풀이

```python
import sys

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
print(min(number) * max(number))
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145414562-d6faf95a-3a51-4629-9116-4440ecfeb329.png)
