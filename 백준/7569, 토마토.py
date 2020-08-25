from _collections import deque

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]  # 상 하 좌 우 윗층 아래층


def ripen(ripened_tomato_list):
    global cnt
    if ripened_tomato_list:
        cnt += 1
    else:
        return
    q = deque(ripened_tomato_list)

    next_q = []
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < H and 0 <= ny < M and 0 <= nz < N:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = 1
                    next_q.append((nx, ny, nz))

    ripen(next_q)


def check_ripen():
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if box[i][j][k] == 0:
                    return -1

    return cnt


# 시작!!!!!!!!!!!!!!!!!!!!!!!!!!
N, M, H = map(int, input().split())
box = []
# 토마토 상자 채우기
for i in range(H):
    step = [list(map(int, input().split())) for _ in range(M)]
    box.append(step)

# 날짜 카운트
cnt = -1

q = []
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 1:
                q.append((i, j, k))

ripen(q)

answer = check_ripen()
print(answer)
