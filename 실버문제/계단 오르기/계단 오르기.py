import sys

n = int(sys.stdin.readline())
stair_list = [0] + [int(sys.stdin.readline()) for _ in range(n)]    # 각 계단이 가지고있는 점수에 대한 list

try:
    score = [0, stair_list[1], stair_list[1] + stair_list[2]]   # 피보나치처럼 처음 0,1,2 번 인덱스의 값은 미리 정해준다.
    for i in range(3, n + 1):   # 3부터 시작
        score.append(max(score[i - 2], score[i - 3] + stair_list[i - 1]) + stair_list[i])   # 이전까지의 총합과 계단의 점수
    print(score[-1])
except IndexError:  # 만약 n == 1일 경우 IndexError 발생
    print(stair_list[-1])