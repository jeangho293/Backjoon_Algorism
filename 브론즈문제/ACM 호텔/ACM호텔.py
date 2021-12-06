for _ in range(int(input())):
    h, w, n = map(int, input().split())
    fast_room = [[[floor, room] for room in range(1, w + 1)] for floor in range(1, h + 1)]  # 방의 층, 호수를 2차원배열로 정리
    fast_room = sum(list(map(list, zip(*fast_room))), [])   # 1차원 배열로 변환하되, 행과 열을 서로 바꾼다.
    target_floor, target_room = fast_room[n - 1]    # --> 그 결과, 손님들이 입실하는 순서로 방이 나열된다.
    print(str(target_floor) + str(target_room).zfill(2))    # zfill(a)는 a의 크기를 갖게 만들며 크기가 작을 경우 왼쪽에서부터 0을 채움