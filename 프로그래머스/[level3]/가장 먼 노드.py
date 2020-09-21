from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    adj = defaultdict(list)
    for e in edge:
        s,e = e
        adj[s].append(e)
        adj[e].append(s)

    visited = [0]*(n+1)
    visited[1] = 1
    q = deque([1])
    while q:
        c = q.popleft()
        for nei in adj[c]:
            if not visited[nei]:
                visited[nei] = visited[c] + 1
                q.append(nei)

    answer = visited.count(max(visited))
    return answer


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))