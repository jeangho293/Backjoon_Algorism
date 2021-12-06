import re
import sys

bracket = {'(': ')', '[': ']'}  # key-value
while True:
    string = sys.stdin.readline().rstrip()  # 오른쪽 공백은 제거
    if string == '.':   # 입력의 끝을 표현
        break
    stack, string_list = [], []

    for s in re.sub('[\w.]', '', string):   # 정규표현식
        if s != ' ':
            string_list.append(s)

    if len(string_list) % 2 == 0:   # 길이가 짝수여야 짝이 맞는다
        for i in string_list:
            try:
                if not stack:   # stack이 비어있으면 첫 요소 append 해준다.
                    stack.append(i)
                else:
                    if bracket[stack[-1]] == i:
                        stack.pop()
                    else:
                        stack.append(i)
            except:
                break
    else:   # 길이가 홀수면 짝이 절대 맞지 않는다. 주의 continue 필수
        print('no')
        continue
    if stack:   # stack에 남아있으면 짝이 안맞아서 남아있다는 의미
        print('no')
    else:
        print('yes')