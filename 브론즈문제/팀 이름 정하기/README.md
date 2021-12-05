
# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1296

난이도 : __브론즈 1__

## 요점

- `Counter` 라이브러리를 활용한 문제 풀이
- `Counter` 타입은 **+, -** 연산이 가능하다. 단, /, * 은 불가능
- 정렬을 위한 `sort()` 함수와 정렬의 기준이 되는 option인 `key`를 사용.  `lambda`를 통해 다수의 조건에 대한 정렬

## 풀이

```python
from collections import Counter # dictionary counter 라이브러리

name = Counter(input()) # 연두의 이름을 입력받자마자 Counter 형으로 변환
team_list = [input() for _ in range(int(input()))]  # list comprehension
best_name = []   # score를 저장하기 위한 배열

for team in team_list:
    result = Counter(team) + name   # Counter 타입끼리의 연산
    score = ((result['L'] + result['O']) * (result['L']+result['V']) * (result['L'] + result['E']) * (result['O'] + result['V'])
             * (result['O']+result['E']) * (result['V'] + result['E'])) % 100   # 점수 구하기
    best_name.append((team, score))
print(sorted(best_name, key=lambda x: (-x[1], x[0]))[0][0]) # 확률이 높은 순으로 정렬하되 중복 점수가 있을 경우, 사전순으로 정렬

```


## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144750060-ceb81b84-8aba-4fea-bf44-d00b812a3a8d.png)
