import heapq
import sys

if __name__ == "__main__":
    N = int(input())
    heap = []
    for i in range(N):
        x = int(sys.stdin.readline())
        if x:
            heapq.heappush(heap, x)
        else:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
