V, E = 6, 11
edges = [
    [0, 1, 3],
    [0, 2, 5],
    [1, 2, 2],
    [1, 3, 6],
    [2, 1, 1],
    [2, 3, 4],
    [2, 4, 6],
    [3, 4, 2],
    [3, 5, 3],
    [4, 0, 3],
    [4, 5, 6]
]

# 인접리스트 만들기
adj = {x: [] for x in range(V)}
for edge in edges:
    s, e, c = edge
    adj[s].append([e, c])

# dist, visited
dist = [float('inf')] * V
visited = [False] * V

# 시작점 선택, 모든 정점 선택
dist[0] = 0
cnt = 0
while cnt < V:
    # dist가 최소인 정점 찾기
    min_dist = float('inf')
    u = -1
    for i in range(V):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    # 정점을 하나 선택
    visited[u] = True

    # 간선 완화
    for w, cost in adj[u]:  # 도착정점, 가중치
        if dist[u] + cost < dist[w]:
            dist[w] = dist[u] + cost
    cnt += 1

print(dist)
