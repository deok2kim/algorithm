import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def dij(d):
    key = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, d))
    key[d] = 0
    while pq:
        cost, node = heapq.heappop(pq)

        if key[node] < cost:
            continue

        for next_node, next_cost in adj[node]:
            if cost + next_cost < key[next_node]:
                key[next_node] = cost + next_cost
                heapq.heappush(pq, (key[next_node], next_node))

    return key


if __name__ == '__main__':
    N, E = map(int, input().split())
    adj = {x + 1: [] for x in range(N)}
    for _ in range(E):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))

    v1, v2 = map(int, input().split())
    # 1번에서 N번까지 v1, v2를 지나서

    # 1에서 v1, 1에서 v2
    # v1 - v2
    # v1에서 N, V2에서 N

    # 시나리오 1: 1 - v1 - v2 - N
    # 시나리오 2: 1 - v2 - v1 - N
    k_1 = dij(1)
    k_v1 = dij(v1)
    k_v2 = dij(v2)

    answer = min(k_1[v1] + k_v1[v2] + k_v2[N], k_1[v2] + k_v2[v1] + k_v1[N])
    if answer < INF:
        print(answer)
    else:
        print(-1)
