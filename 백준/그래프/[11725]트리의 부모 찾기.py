from _collections import deque
N = int(input())
adj = {i: [] for i in range(1,N+1)}
for _ in range(N-1):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visit = [False]*(N+1)
parents = [0]*(N+1)
q = deque()

q.append(1)
visit[1] = True
while q:
    cur = q.popleft()
    for neighbor in adj[cur]:
        if not visit[neighbor]:
            q.append(neighbor)
            visit[neighbor] = True
            parents[neighbor] = cur

for i in range(2, N+1):
    print(parents[i])
