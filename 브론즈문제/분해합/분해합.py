n = input()

result, number_n = 0, int(n)
min_number = 0 if number_n - (len(n) * 9) < 0 else number_n - (len(n) * 9)  # 음수일 경우 min은 0으로 정의한다. 예외 처리임
for i in range(min_number, number_n + 1):
    if i + sum(map(int, str(i))) == number_n:   # map과 sum을 통한 pythonic한 코딩
        result = i
        break
print(result)