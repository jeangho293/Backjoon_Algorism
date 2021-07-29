import sys

while True:
    string = sorted([sys.stdin.readline().rstrip() for _ in range(int(input()))], key=lambda x: x.lower())
    if not string:
        break
    print(string[0])