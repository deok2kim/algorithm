import heapq

if __name__ == '__main__':
    N, M = map(int, input().split())  # 문제는 1부터 시작이므로 -1 해줌
    room = [list(map(int, input())) for _ in range(M)]

    # 가중치 2차원 배열
    key = [[float('inf')] * N for _ in range(M)]

    pq = []
    heapq.heappush(pq, (0, 0, 0))
    key[0][0] = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while pq:
        cost, x, y = heapq.heappop(pq)
        if x == M - 1 and y == N - 1:
            print(key[x][y])
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                # 다음 갈 곳이 벽이고, 현재 가는 루트의 비용이 더 작다면 고
                if room[nx][ny] == 1 and cost + 1 < key[nx][ny]:
                    heapq.heappush(pq, (cost + 1, nx, ny))
                    key[nx][ny] = cost + 1
                # 다음 갈 곳이 룸이고, 현재 가는 루트의 비용이 더 작다면 고
                elif room[nx][ny] == 0 and cost < key[nx][ny]:
                    heapq.heappush(pq, (cost, nx, ny))
                    key[nx][ny] = cost
