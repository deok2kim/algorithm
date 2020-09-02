from collections import deque
import sys


def bfs(x, y):
    q = deque()
    visited = set()
    q.append((x,y))
    visited.add((x,y))
    while q:
        # print(q)
        x, y = q.popleft()
        if x == x1 and y == y1:
            print('happy')
            return

        for nx, ny in stores:
            if (nx, ny) not in visited:
                if abs(x-nx) + abs(y-ny) <= 50*20:
                    q.append((nx, ny))
                    visited.add((nx, ny))
    print('sad')
    return


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        n = int(input())  # 편의점 개수

        x, y = map(int, input().split())  # HOME
        stores = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        x1, y1 = map(int, input().split())
        stores.append([x1, y1])

        bfs(x,y)
