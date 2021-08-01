target = int(input())

def Prime_search(target):
    _prime = [True] * (target + 1)

    for i in range(2, int(target ** 0.5) + 1):
        if _prime[i]:
            for j in range(i * i, target + 1, i):
                _prime[j] = False

    return [i + 2 for i, value in enumerate(_prime[2:]) if value]


def check_number(number):
    check = set()
    p_list = list(str(number))

    while 1 not in check:           # 최종 1이 된다면 while문을 탈출
        result = 0
        for i in p_list:
            result += int(i) ** 2

        # 중복된 수인지를 확인하는 로직
        if result in check:         # 중복된 수이므로 상근수가 될 수 없다.
            return False
        else:
            check.add(result)       # 중복된 수가 아니면 check.add 를 해주고 p_list도 변환
            p_list = list(str(result))

    return True


prime = Prime_search(target)
for p in prime:
    if check_number(p):
        print(p)