for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x  # 두 행성 사이의 거리
    if distance < 4:
        print(distance)
    else:
        number = int(distance ** 0.5)   # 횟수는 거리의 제곱근 +- 1 사이에서 결정되어진다.
        if distance == number ** 2:     # 완전제곱수일 경우, 횟수가 딱 바뀌는 지점이므로 거리 제곱근 * 2 - 1
            print(2 * number - 1)
        elif number ** 2 < distance <= number ** 2 + number:    # 사이에 존재할 경우, 2 * 거리 제곱근
            print(2 * number)
        else:   # 그 외의 경우는 이동거리가 1번 더 많은 경우다.
            print(2 * number - 1)
