n = int(input())
call_times = list(map(int, input().split()))

Y, M = 0, 0
for time in call_times:
    Y += (10 * ((time // 30) + 1))  # Y의 요금 합
    M += (15 * ((time // 60) + 1))  # M의 요금 합

if Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)
else:
    print('Y M', Y)