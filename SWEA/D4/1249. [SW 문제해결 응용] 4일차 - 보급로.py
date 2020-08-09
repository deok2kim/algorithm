from _collections import deque

for tc in range(1, 1 + int(input())):
    n = int(input())
    maps = [list(map(int, list(input()))) for _ in range(n)]

    answer = 0
    # keys: 최소값을 누적할 리스트
    # 각 지점은 그 지점까지 오는데 드는 시간을 누적
    keys = [[99999] * n for _ in range(n)]
    keys[0][0] = 0  # 시작점은 0
    q = deque()
    q.append((0, 0))

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                # 현재 지점의 값 + 다음 지점을 가는데 필요한 값 < 다음 지점의 값
                # 을 비교한다.
                if keys[x][y] + maps[nx][ny] < keys[nx][ny]:
                    keys[nx][ny] = keys[x][y] + maps[nx][ny]
                    q.append((nx, ny))

    answer = keys[-1][-1]

    print('#{} {}'.format(tc, answer))
