from heapq import heappop, heappush
import sys

heap_list = []
for _ in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())
    if not number:
        try:
            print(heappop(heap_list)[1])
        except:
            print(0)
    else:
        heappush(heap_list, (abs(number), number))