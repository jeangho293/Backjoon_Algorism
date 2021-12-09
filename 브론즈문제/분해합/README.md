# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/2231

난이도 : __브론즈 2__

## 요점

- `완전 탐색`문제
1. 0~n 까지의 경우에 대해서 완전 탐색을 하는 방법 --> 1500ms의 시간이 걸린다.
2. min~n 까지의 경우에 대해서 완전 탐색을 하는 방법 --> 70ms의 시간이 걸린다.
    - min을 구하는 방법에 대해서
    
      문제의 예시 중 216의 min은 216 - (총 자릿수 * 9)라고 할 수 있다. 왜냐하면 세자릿수가 가질 수 있는 최대의 수는 999 이므로 최대 27만큼 - 할 수 있다.
    
    - **단 예외 케이스가 존재**하는데 그 경우는 n이 1~17일 경우, __min값이 음수__ 가 된다. 예외 처리 필수
## 풀이
    
```python
n = input()

result, number_n = 0, int(n)
min_number = 0 if number_n - (len(n) * 9) < 0 else number_n - (len(n) * 9)  # 음수일 경우 min은 0으로 정의한다. 예외 처리임
for i in range(min_number, number_n + 1):
    if i + sum(map(int, str(i))) == number_n:   # map과 sum을 통한 pythonic한 코딩
        result = i
        break
print(result)
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145389284-f31ebe8c-d5a4-42ca-9223-35026b0a87c9.png)
