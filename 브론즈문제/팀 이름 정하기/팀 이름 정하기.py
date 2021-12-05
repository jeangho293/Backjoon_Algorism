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
