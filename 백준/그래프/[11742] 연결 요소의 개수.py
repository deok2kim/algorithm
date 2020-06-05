from _collections import deque


def bfs(vertex):

    q = deque()
    q.append(vertex)
    while q:
        current = q.popleft()
        visit[current] = True
        for neighbor in adj[current]:
            if visit[neighbor] is False:
                q.append(neighbor)
                visit[neighbor] = True
    return


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visit = [False]*(n+1)
cnt = 0

for i in range(1, n+1):
    if visit[i] is False:
        bfs(i)
        cnt += 1

print(cnt)
