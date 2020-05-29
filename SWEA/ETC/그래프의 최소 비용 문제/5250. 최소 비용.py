import heapq

for tc in range(1, int(input()) + 1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # BFS 탐색을 하기 위한
    key = [[float('inf')]*n for _ in range(n)]  # 시작점에서 특정배열에 도달하기 위한 최소 연료 값을 저장할 배열 | float('inf') 는 파이썬 최대값
    dijk = [[False]*n for _ in range(n)]  # visit 배열과 같은 개념
    pq = []

    key[0][0] = 0  # 0,0 에서 0 까지 도달하기 위한 연료는 0이므로 초기화
    heapq.heappush(pq, (0, 0, 0))

    while True:
        w, cx, cy = heapq.heappop(pq)  # 그 점의 도달하기 위한 비용, 그점의 좌표
        if cx == n-1 and cy == n-1:  # 체크할 현재위치가 최종도착점이라면 break
            break

        if dijk[cx][cy]:
            continue

        dijk[cx][cy] = True  # 아니라면 방문 표시

        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0 <= nx < n and 0 <= ny < n and not dijk[nx][ny]:
                cost = key[cx][cy] + 1  # 현재 위치까지 도달하기 위한 비용 + 1
                # 다음 지점이 현재 지점보다 높으면 높이차이를 더해준다.
                if maps[cx][cy] < maps[nx][ny]:
                    cost += maps[nx][ny] - maps[cx][cy]

                # 한 점에 도달하는 경우의 수는 보통 4가지이다.
                # 그로므로 하상 최소값으로 갱신해준다.
                if cost < key[nx][ny]:
                    key[nx][ny] = cost
                    heapq.heappush(pq, (cost, nx, ny))

    # for row in key:
    #     print(row)
    print('#{} {}'.format(tc, key[n-1][n-1]))
