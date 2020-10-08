import sys
import heapq

N = int(input())
numbers = []
for i in range(N):
    number = int(sys.stdin.readline())
    if number:
        heapq.heappush(numbers, -number)
    else:
        if numbers:
            print(abs(heapq.heappop(numbers)))
        else:
            print(0)
