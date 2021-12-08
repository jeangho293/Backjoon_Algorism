# 풀이 :notebook:

   문제 링크 : https://www.acmicpc.net/problem/2798

   난이도 : __브론즈 2__
   
##요점
- `완전 탐색`문제이지만 `투 포인터 기법`을 활용하면 효율적으로 풀이

- 투 포인트란?

    `인덱스의 시작` 과 `끝 점`을 문제에 맞게 설정하여 연속적인 합이나 특정 갯수의 합(최대 3개가 적당)에 대해 알맞다고 생각된다.

## 풀이

```python
import sys

# 투 포인터 형식의 문제 풀이
def best_card_sum(card_list, length):
    result = []
    for first in range(length - 2):     # first는 고정된 카드
        left, right = first + 1, length - 1

        while left < right:     # left 와 right 눈 card_sum 에 따라 유동적으로 변한다.
            card_sum = card_list[first] + card_list[left] + card_list[right]    # 세 카드의 합
            if card_sum == target:  # 만약 세 카드의 합이 target 과 같으면 해당 함수 종료
                print(target)
                return
            elif card_sum > target:     # 세 카드의 합은 target보다 클 수 없으니 right를 -1 이동
                right -= 1
            else:
                result.append(card_sum)     # 세 카드의 합이 target 보다 작으면 우선 result 리스트에 추가
                left += 1       # 더 가까운 수가 있을 수 있으니 left를 +1 이동
    print(sorted(result)[-1])       # 11번째 줄에서 함수 return이 없으면 여기서 가장 근접한 수를 추출한다.


n, target = map(int, sys.stdin.readline().split())
card_list = sorted(list(map(int, sys.stdin.readline().split())))    # 투 포인터를 사용하기위해서는 사전 정렬이 필요

best_card_sum(card_list, len(card_list))
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/145176096-dceedc24-9eeb-4ccb-8dc6-5f51a5d39f38.png)
