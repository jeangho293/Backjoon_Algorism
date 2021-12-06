import sys
stack = []
for _ in range(int(sys.stdin.readline().rstrip())):
    number = int(sys.stdin.readline().strip())
    if number != 0:
        stack.append(number)
    else:
        stack.pop()
print(sum(stack))