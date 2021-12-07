import sys

n, money = map(int, sys.stdin.readline().split())
money_list = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0     # 총 동전의 갯수
for i in range(n - 1, -1, -1):
    q, money = divmod(money, money_list[i])     # divmod를 활용하여 몫과 나머지 전부 구함
    cnt += q
    if not money:   # 바꿔먹을 돈이 없으면 loof 문 탈출
        break
print(cnt)
