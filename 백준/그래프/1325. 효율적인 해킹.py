import sys
from collections import defaultdict
from collections import deque


def bfs(start):
    q = deque([start])
    visited = [0] * (N + 1)
    visited[start] = 1
    cnt = 0
    while q:
        c = q.popleft()
        cnt += 1
        for nei in adj[c]:
            if not visited[nei]:
                q.append(nei)
                visited[nei] = 1

    return cnt


input = sys.stdin.readline

N, M = map(int, input().split())

adj = defaultdict(list)
for _ in range(M):
    e, s = map(int, input().split())
    adj[s].append(e)

print(adj)

result = []
for i in range(1, N + 1):
    result.append([bfs(i), i])

print(result)

result.sort(key=lambda x: (-x[0], x[1]))

max_cnt = result[0][0]
for r in result:
    if r[0] == max_cnt:
        print(r[1], end=" ")
    else:
        break
