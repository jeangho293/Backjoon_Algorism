# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/11729
   
   난이도 : __실버 2__
   
##요점

- `재귀 함수`를 이용한 풀이법

## 풀이

```python
import sys

n = int(sys.stdin.readline())
moves = []      # 이동 경로


# 하노이의 탑 재귀 함수
def hanoi(n, one, two, three):
    if n == 1:
        moves.append([one, three])
    else:
        hanoi(n - 1, one, three, two)
        moves.append([one, three])
        hanoi(n - 1, two, one, three)


hanoi(n, 1, 2, 3)
print(len(moves))
for move in moves:
    print(move[0], move[1])

```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/146664364-e01bbbfd-6064-4533-b95c-3d9a9a748f86.png)
