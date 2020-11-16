from itertools import combinations
from collections import deque



def solution(n, edges):
    answer = 0

    adj = {x + 1: [] for x in range(n)}
    for edge in edges:
        s, e = edge
        adj[s].append(e)
        adj[e].append(s)

    print(adj)

    for combi in combinations(range(1,n+1), 3):
        print(combi)
        a,b,c = combi
        total = 0

        b_flag = False
        c_flag = False
        # a에서 b,c
        q = deque()
        q.append(a)
        visited = [-1]*(n+1)
        visited[a] = 0
        while q:
            cur = q.popleft()
            for naver in adj[cur]:
                if visited[naver] == -1:
                    q.append(naver)
                    visited[naver] = visited[cur] + 1
                    if naver == b:
                        b_flag = True
                        total += visited[naver]
                    if naver == c:
                        c_flag = True
                        total += visited[naver]

            if b_flag and c_flag:
                break
        print(visited)
        # b에서 c
        q = deque()
        q.append(b)
        visited = [-1] * (n + 1)
        visited[b] = 0
        while q:
            cur = q.popleft()
            for naver in adj[cur]:
                if visited[naver] == -1:
                    q.append(naver)
                    visited[naver] = visited[cur] + 1
                    if naver == a:
                        total += visited[naver]
        print(visited)
        print(total//3)
        total = total//3
        answer = max(answer, total)

    return answer


print(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]))
