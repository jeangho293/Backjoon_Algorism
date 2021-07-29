import sys, re

stack = []
for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline().rstrip()
    number = list(map(int, re.findall('[0-9]', string)))
    stack.append((string, sum(number)))

for s in sorted(stack, key=lambda x: (len(x[0]), x[1], x[0])):
    print(s[0])