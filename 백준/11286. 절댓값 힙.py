import sys
import heapq
N = int(input())
q = []
for tc in range(N):
    number = int(sys.stdin.readline())
    if number:
        heapq.heappush(q, (abs(number), number))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
