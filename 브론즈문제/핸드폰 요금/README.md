# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1267

난이도 : __브론즈 3__

## 요점

- **나머지 연산** 과 관련된 문제

## 풀이

```python
n = int(input())
call_times = list(map(int, input().split()))

Y, M = 0, 0
for time in call_times:
    Y += (10 * ((time // 30) + 1))
    M += (15 * ((time // 60) + 1))

if Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)
else:
    print('Y M', Y)
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144750731-c9a78a46-62f1-454a-97c6-5ed7807a284f.png)