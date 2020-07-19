import heapq

for tc in range(1, 1+int(input())):
    n = int(input())
    maps = [list(map(int, list(input()))) for _ in range(n)]

    # dist: 가중치를 누적한 리스트, visit: 선택했는지 안했는지
    dist = [[float('inf')]*n for _ in range(n)]
    visit = [[False]*n for _ in range(n)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    pq = []
    # 0, 0부터 시작
    heapq.heappush(pq, (0, 0, 0))
    dist[0][0] = 0
    while pq:
        w, x, y = heapq.heappop(pq)

        # 이미 선택했었다면 continue
        if visit[x][y]:
            continue

        # 끝 점에 도착
        if x == n-1 and y == n-1:
            break

        # 선택하지 않았었다면 시작
        visit[x][y] = True

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and w < dist[nx][ny]:
                    dist[nx][ny] = maps[nx][ny] + w
                    heapq.heappush(pq, (dist[nx][ny], nx, ny))

    print('#{} {}'.format(tc, dist[-1][-1]))
