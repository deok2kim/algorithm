from collections import deque


def solution(N, M, compare):
    answer = 0
    heavy_adj = {x + 1: [] for x in range(N)}
    light_adj = {x + 1: [] for x in range(N)}

    for h, l in compare:
        heavy_adj[l].append(h)
        light_adj[h].append(l)

    for i in range(1, N + 1):
        visited = [0]*(N+1)
        q = deque([i])
        cnt = 0
        while q:
            c = q.popleft()
            for nei in heavy_adj[c]:
                if visited[nei] == 0:
                    visited[nei] = True
                    q.append(nei)
                    cnt += 1

        if cnt > N // 2:
            answer += 1
        visited = [0] * (N + 1)
        q.append(i)
        cnt = 0
        while q:
            c = q.popleft()
            for nei in light_adj[c]:
                if visited[nei] == 0:
                    visited[nei] = True
                    q.append(nei)
                    cnt += 1

        if cnt > N // 2:
            answer += 1

    print(answer)


if __name__ == "__main__":
    N0, M0 = map(int, input().split())
    compare0 = [list(map(int, input().split())) for _ in range(M0)]
    solution(N0, M0, compare0)
