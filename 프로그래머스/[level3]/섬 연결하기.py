import heapq as h
from collections import defaultdict


def solution(n, costs):
    answer = 0

    # adj = [[0]*n for _ in range(n)]
    # for cost in costs:
    #     adj[cost[0]][cost[1]] = cost[2]
    adj = defaultdict(list)
    for cost in costs:
        adj[cost[0]].append([cost[1], cost[2]])
        adj[cost[1]].append([cost[0], cost[2]])

    # print(adj)

    pq = []
    visited = [0] * n
    visited[0] = 1

    for neighbor in adj[0]:
        h.heappush(pq, (neighbor[1], neighbor[0]))

    # print(pq)

    while pq:
        cost, start = h.heappop(pq)
        print(cost,start, visited)

        if visited[start]:
            continue

        for neighbor in adj[start]:
            if not visited[neighbor[0]]:
                h.heappush(pq, (neighbor[1], neighbor[0]))

        answer += cost
        visited[start] = 1

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
