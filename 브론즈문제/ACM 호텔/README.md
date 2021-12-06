# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/10250

난이도 : __브론즈 3__

## 요점

- `zip`을 활용하여 **행과 열**을 바꾼다.
- 2차원을 1차원 배열로 만드는 방법은 여러가지가 존재함.
  1. `array1 = sum(array2, [])` --> 가장 추천
  2. `import itertools`를 활용하여 만들 수도 있다.
     1. `list(itertools.chain.from_iterable(array2))`
  3. `reduce`도 가능하다.
- 본인은 이렇게 문제를 풀었지만 생각해보니 몫과 나머지로 구할 수도 있을 것 같다.(해보지는 않음)

## 풀이

```python
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    fast_room = [[[floor, room] for room in range(1, w + 1)] for floor in range(1, h + 1)]  # 방의 층, 호수를 2차원배열로 정리
    fast_room = sum(list(map(list, zip(*fast_room))), [])   # 1차원 배열로 변환하되, 행과 열을 서로 바꾼다.
    target_floor, target_room = fast_room[n - 1]    # --> 그 결과, 손님들이 입실하는 순서로 방이 나열된다.
    print(str(target_floor) + str(target_room).zfill(2))    # zfill(a)는 a의 크기를 갖게 만들며 크기가 작을 경우 왼쪽에서부터 0을 채움
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144793810-e9ec65c0-9dba-4ae9-842b-476e2470327d.png)