# 풀이 :notebook:

문제 링크 : https://www.acmicpc.net/problem/1076

난이도 : __브론즈 2__

## 요점

- `dictionary` 타입으로 key-value 로 선언
- 마지막 색깔에 대해서는 제곱 연산이므로 `10 ** a` 또는 `pow(10, a)` 사용

## 풀이

```python
resistance = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
              'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}    # dictionary 형식으로 저항값 선언

color_list = [input() for i in range(3)]
print(int(str(resistance[color_list[0]]) + str(resistance[color_list[1]])) * (10 ** resistance[color_list[2]]))
```

## 실행 결과

![image](https://user-images.githubusercontent.com/84619866/144750374-71b1d0c5-8613-46d3-9d9f-a73542b58237.png)
