import sys

n, m = map(int, sys.stdin.readline().split())
best_6, best_1 = 1001, 1001

for _ in range(m):                              # 각각의 기타줄에 대해 가장 저렴한 브랜드를 구한다.
    line_6, line_1 = map(int, sys.stdin.readline().split())
    best_6, best_1 = min(line_6, best_6), min(line_1, best_1)

if best_6 / 6 >= best_1:                    # 1개당의 효율이 best_1 이 가장 저렴하다면 모든 기타줄은 best_1 가격으로 구매한다.
    print(n * best_1)
else:
    need_money = n // 6 * best_6            # n // 6 몫만큼 best_6 가격으로 구매하고 나머지에 대한 비교를 한다.
    if best_6 <= (n % 6) * best_1:          #  n % 6 개에 대하여 기타줄 6개 한세트를 사는 것과 기타줄 1개씩 사는 것을 비교한다.
        need_money += best_6
    else:
        need_money += (n % 6) * best_1
    print(need_money)