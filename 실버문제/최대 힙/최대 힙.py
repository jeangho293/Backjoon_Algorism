from heapq import heappush, heappop
import sys

heap_list = []
for _ in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())
    if not number:
        try:
            print(-heappop(heap_list))
        except:
            print(0)
    else:
        heappush(heap_list, -number)