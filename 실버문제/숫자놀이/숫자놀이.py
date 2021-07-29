number = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
          '8': 'eight', '9': 'nine', '0': 'zero'}

stack = []
a, b = map(int, input().split())

for i in range(a, b + 1):
    string = ''
    for j in list(str(i)):
        string += number[j]
    stack.append((i, string))

for i, s in enumerate(sorted(stack, key=lambda x: x[1]), start=1):
    print(s[0], end=' ')
    if i % 10 == 0:
        print()