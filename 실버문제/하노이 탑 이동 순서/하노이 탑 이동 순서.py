import sys

n = int(sys.stdin.readline())
moves = []      # 이동 경로


# 하노이의 탑 재귀 함수
def hanoi(n, one, two, three):
    if n == 1:
        moves.append([one, three])
    else:
        hanoi(n - 1, one, three, two)
        moves.append([one, three])
        hanoi(n - 1, two, one, three)


hanoi(n, 1, 2, 3)
print(len(moves))
for move in moves:
    print(move[0], move[1])
