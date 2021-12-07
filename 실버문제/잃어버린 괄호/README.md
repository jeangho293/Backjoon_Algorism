# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1541

난이도 : __실버 2__

## 요점

- `그리드 알고리즘` 문제

이 문제의 규칙이 존재한다.

**첫 - 연산자가 나오는 시점부터 그 뒤의 모든 숫자는 -를 붙이는 것과 같다** 것이 이 문제의 요점이다.
![KakaoTalk_20211207_175856145](https://user-images.githubusercontent.com/84619866/144998649-3b72406b-9680-431f-9913-ece69fabe9de.jpg)




## 풀이

```python
import sys
import re

string = sys.stdin.readline().rstrip()
first_minus_location = string.find('-') # - 연산자가 존재하는지 찾는다. 존재하지 않으면 -1값이 나옴

if first_minus_location != -1:  # 연산식에 - 라는 연산자가 존재하면, 
    positive_number = map(int, string[:first_minus_location].split('+'))    # 첫 -이전까지 연산자 +를 기준으로 split
    negative_number = map(int, re.sub('[\-+]', ' ', string[first_minus_location + 1:]).split()) # 첫 - 이후부터 연산자 -와 +를 기준으로 split
    print(sum(positive_number) - sum(negative_number))  # 합
else:   # 연산식에 - 라는 연산자가 없으면 모두 +으로 이루어진 연산식이다.
    positive_number = map(int, string.split('+'))
    print(sum(positive_number))
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144996942-3ba9d15b-a2bd-4e9e-b134-1e189b5e549e.png)
