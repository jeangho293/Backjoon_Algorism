# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/10773
   
   난이도 : __실버 4__
   
##요점

- 자료구조 `stack`문제

## 풀이
```python
import sys  # 입력값 받기 위한 라이브러리 --> 이게 빠름

stack = []
for _ in range(int(sys.stdin.readline().rstrip())):
    number = int(sys.stdin.readline().strip())
    if number != 0: # number 가 0이 아니면 stack 추가
        stack.append(number)
    else:   # 0일 경우 stack에서 한개 제외
        stack.pop()
print(sum(stack))
   ```
   
## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144881582-9df74676-1aee-4a26-af69-06c410dbb636.png)