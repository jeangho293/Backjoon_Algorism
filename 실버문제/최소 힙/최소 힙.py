from heapq import heappop, heappush         # heap 구현을 위한 built-in 함수
import sys

heap_list = []
for _ in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())
    if number == 0:
        try:                                # try - except 을 활용하여 IndexError(비어있는 경우) 처리
            print(heappop(heap_list))       # 힙 출력
        except:
            print(0)
    else:
        heappush(heap_list, number)         # 힙 삽입