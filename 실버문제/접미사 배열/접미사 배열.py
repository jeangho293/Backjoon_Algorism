import sys

string = sys.stdin.readline().rstrip()
for s in sorted([string[i:] for i in range(len(string))]):
    print(s)