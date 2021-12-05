n = input()

# 만약 주어진 수가 0~9일 경우, 0을 덧붙인다.
if len(n) == 1:
    n = '0' + n

temp, cnt = n, 0    # 원래의 숫자를 임시 저장, 사이클 횟수 선언
while True:
    first_number = n[-1]    # 2번째 자릿수
    second_number = str(int(n[0]) + int(n[1]))  # 1번째 자릿수
    n = first_number + second_number[-1]    # 결과
    cnt += 1
    if temp == n:
        print(cnt)
        break