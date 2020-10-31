import sys
import heapq

input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N):
    heapq.heappush(numbers, int(input()))

while numbers:
    print(heapq.heappop(numbers))
