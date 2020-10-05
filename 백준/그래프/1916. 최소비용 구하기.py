import sys
import heapq as h

input = sys.stdin.readline


def dijkstra(S, E):
    pq = []
    h.heappush(pq, (0, S))
    visited = [0] * (N + 1)
    key = [float('inf')] * (N + 1)
    key[S] = 0
    while pq:
        k, u = h.heappop(pq)

        if visited[u]:
            continue

        visited[u] = 1
        for nei_u, nei_k in adj[u]:
            if not visited[nei_u] and k + nei_k < key[nei_u]:
                key[nei_u] = k + nei_k
                h.heappush(pq, (key[nei_u], nei_u))
    print(key[E])


if __name__ == '__main__':
    N = int(input())  # 도시의 개수
    M = int(input())  # 버스의 개수

    adj = {x + 1: [] for x in range(N)}
    for bus in range(M):
        s, e, k = map(int, input().split())
        adj[s].append((e, k))

    A, B = map(int, input().split())

    dijkstra(A, B)
