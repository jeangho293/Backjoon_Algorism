n = int(input())

# 그리드 문제
max_only_five = n // 5  # 5kg 의 봉지로 나눴을 때, 최대
result = -1
while max_only_five >= 0:   # 갯수가 0이상 일때만 while문 실행
    sugar = max_only_five * 5   # 5kg으로 포장되어진 설탕의 갯수
    rest_sugar = n - sugar  # 5kg으로 포장되고 남은 설탕의 갯수
    if rest_sugar % 3 == 0: # 남은 설탕의 갯수가 3으로 나누어 떨어지는가?
        result = max_only_five + rest_sugar // 3    # 나눠떨어지면 그게 최솟값
        break
    max_only_five -= 1  # 나눠떨어지지않는다면 5kg 봉지를 하나 줄인다.

print(result)