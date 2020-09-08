import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    adj = {x + 1: [] for x in range(N)}
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    visited = [-1] * (N + 1)
    q = deque([1])
    visited[1] = 0
    while q:
        c = q.popleft()
        for n in adj[c]:
            if visited[n] == -1:
                q.append(n)
                visited[n] = visited[c] + 1

    max_num = max(visited)
    idx = visited.index(max_num)
    cnt = visited.count(max_num)

    print(idx, max_num, cnt)
