import sys
from collections import deque

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    adj = {x + 1: [] for x in range(n)}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    # print(adj)
    visited = [0] * (n + 1)
    visited[1] = 1
    q = deque([1])

    while q:
        c = q.popleft()
        for friend in adj[c]:
            if not visited[friend]:
                visited[friend] = visited[c] + 1
                q.append(friend)
    # print(visited)
    print(len(list(filter(lambda x: 1 < x < 4, visited))))
