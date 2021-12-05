# 풀이 :notebook:

문제 링크 : 

난이도 : __브론즈 1__

## 요점

- **등차수열** 문제

## 풀이

```python
N = int(input())

first_number, increase_number = 5, 7    # 첫번재 도형, 첫번째로 증가하는 숫자

for i in range(1, N):
    first_number += increase_number
    increase_number += 3    # 규칙상 7, 10, 13, 16 ... 으로 증가하는 등차수열

print(first_number % 45678)
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144750657-78e74404-7ef7-4a94-9a0a-c37cca1726c4.png)