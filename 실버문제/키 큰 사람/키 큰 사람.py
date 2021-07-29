import sys

while True:
    info = [list(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))]
    if not info:
        break
    sorted_info = sorted(info, key=lambda x: -float(x[1]))

    for result in sorted_info:
        if result[1] == sorted_info[0][1]:
            print(result[0], end=' ')
        else:
            break
    print()