from _collections import deque


def dfs(V):
    visited[V] = True
    dfs_visit.append(V)
    for neighbor in graph[V]:
        if visited[neighbor] is False:
            dfs(neighbor)


def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = True
    bfs_visit.append(V)

    while q:
        V = q.popleft()
        for neighbor in graph[V]:
            if visited[neighbor] is False:
                visited[neighbor] = True
                q.append(neighbor)
                bfs_visit.append(neighbor)


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = {}
    for i in range(1, N + 1):
        graph[i] = []

    for i in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in graph.keys():
        graph[i].sort()

    visited = [False for _ in range(N + 1)]
    dfs_visit = []
    dfs(V)
    print(' '.join(map(str, dfs_visit)))

    visited = [False for _ in range(N + 1)]
    bfs_visit = []
    bfs(V)
    print(' '.join(map(str, bfs_visit)))
