from collections import defaultdict


def solution(t):
    answer = 0
    adj = defaultdict(list)
    for s, e in t:
        adj[s].append(e)
        adj[e].append(s)

    def dfs(c):
        nonlocal answer
        cnt = 0
        for vis in visited:
            if vis >= 1:
                cnt += 1

        for neighbor in adj[c]:
            if visited[neighbor] < 2:
                visited[neighbor] += 1
                dfs(neighbor)
                visited[neighbor] -= 1

        answer = max(cnt, answer)

    n = len(t) + 1
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        dfs(i)
        visited[i] = 0

    return answer
