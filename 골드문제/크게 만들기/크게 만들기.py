from collections import deque

def solution():
    n, delete = map(int, input().split())
    string = deque(input())

    stack = []
    while string:
        stack.append(string.popleft())

        if stack and string and stack[-1] < string[0]:
            while string and stack and stack[-1] < string[0]:
                stack.pop()
                delete -= 1
                if delete == 0:
                    return ''.join(stack) + ''.join(string)
    return ''.join(stack[:len(stack) - delete])


print(solution())