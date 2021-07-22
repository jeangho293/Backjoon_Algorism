team_number, broken_team_number, spare_team_number = map(int, input().split())

lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

result_reserve = set(reserve) - set(lost)       # 카약을 잃어버린 팀이 여분을 가지고 있는 상황에 대한 처리
result_lost = set(lost) - set(reserve)

for i in result_reserve:                        # 여분을 가지고 있는 팀으로부터 앞뒤의 팀이 잃어버린 경우 처리
    if (i - 1) in result_lost:
        result_lost.remove(i - 1)
    elif (i + 1) in result_lost:
        result_lost.remove(i + 1)
print(len(result_lost))