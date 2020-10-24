def dfs(c):
    print(c, end=' ')
    for neighbor in adj[c]:  # c의 이웃 중
        if visited[neighbor] == 0:  # 방문 아직 안한 친구이면
            visited[neighbor] = 1
            dfs(neighbor)


# 인접리스트
# 노드: 1,2,3,4,5,6,7
n = 10
adj = {x: [] for x in range(1, n + 1)}
edges = [
    [1, 2],
    [1, 5],
    [1, 9],
    [2, 3],
    [3, 4],
    [5, 6],
    [5, 8],
    [6, 7],
    [9, 10]
]

# 무방향 그래프이므로 반대쪽도 성립
for edge in edges:
    s, e = edge
    adj[s].append(e)
    adj[e].append(s)

print(adj)

# 1부터 탐색
k = 1
visited = [0] * (n + 1)
visited[k] = 1
print('방문 순서')
dfs(k)
