from _collections import deque

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    # 인접리스트 생성
    adj = {x + 1: [] for x in range(N)}
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # 방문확인, 큐, 무리의 갯수
    visited = [0] * (N + 1)
    visited[0] = 1
    q = deque()
    cnt = 0

    # 전체 무리를 찾아야 하므로 for문으로 1명씩 큐에 집어넣는다.
    for i in range(1, N+1):
        # 아직 방문하지 않았을 경우에만
        if visited[i] == 0:
            cnt += 1
            q.append(i)
            visited[i] == 1

        # BFS 탐색색
        while q:
            c = q.popleft()
            for neighbor in adj[c]:
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

    print('#{} {}'.format(tc, cnt))
