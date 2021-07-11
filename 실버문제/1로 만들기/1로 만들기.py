# 1로 변환할 수 있는 최소한의 횟수

n = int(input())
cnt = 0

super_node = set([n])
while True:
    if 1 in super_node:
        print(cnt)
        break
    sub_node = set()
    for node in super_node:
        if node % 2 == 0:
            sub_node.add(node // 2)
        if node % 3 == 0:
            sub_node.add(node // 3)
        sub_node.add(node - 1)
    cnt += 1
    super_node = sub_node