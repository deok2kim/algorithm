import sys
import heapq

input = sys.stdin.readline


def dijkstra(s, e):
    pq = []
    heapq.heappush(pq, (0, s))  # 출발지로 가는데 0원의 비용
    visited = [0] * (N + 1)
    while pq:
        cost, w = heapq.heappop(pq)
        if w == e:
            return cost

        if visited[w]:
            continue

        visited[w] = 1
        for newt_w, next_cost in adj[w]:
            if not visited[newt_w]:
                heapq.heappush(pq, (cost + next_cost, newt_w))


if __name__ == '__main__':
    N = int(input())  # 도시의 개수
    M = int(input())  # 버스의 개수
    adj = {x + 1: [] for x in range(N)}
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    departure, arrival = map(int, input().split())
    answer = dijkstra(departure, arrival)
    print(answer)
