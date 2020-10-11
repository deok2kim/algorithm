import heapq


def solution(N, road, K):
    answer = 0

    adj = {x + 1: [] for x in range(N)}
    for r in road:
        s, e, k = r
        adj[s].append([k, e])
        adj[e].append([k, s])

    visited = [0] * (N + 1)

    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        key, node = heapq.heappop(pq)

        if key <= K:
            visited[node] = 1

        for neighbor in adj[node]:
            n_key, n_node = neighbor
            if not visited[n_node] and n_key + key <= K:
                heapq.heappush(pq, [n_key + key, n_node])

    answer = sum(visited)
    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
