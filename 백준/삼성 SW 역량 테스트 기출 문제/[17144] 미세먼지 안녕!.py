def air_purifier():
    # 공기청정기가 바람을 흡수하는 방향으로 진행, 먼지를 한칸 씩 당겨준다.
    for i in range(2):
        x, y = machine[i][0], machine[i][1]
        cx, cy = x, y
        k = 0

        # 위쪽 공기청정기
        if i == 0:
            cx -= 1
            dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 위, 오, 아, 왼 | 시계방향
            while k != 4:
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx <= x and 0 <= ny < C:  # nx가 만족하는 범위는 공기청정기와 벽 사이
                    if home[nx][ny] != -1:
                        home[cx][cy] = home[nx][ny]
                    else:
                        home[cx][cy] = 0  # 마지막 공기청정기를 만났을 때
                    cx, cy = nx, ny
                else:
                    k += 1

        # 아래쪽 공기청정기
        else:
            cx += 1
            dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]  # 아, 오, 위, 왼 | 반시계방향
            while k != 4:
                nx = cx + dx[k]
                ny = cy + dy[k]
                if x <= nx < R and 0 <= ny < C:
                    if home[nx][ny] != -1:
                        home[cx][cy] = home[nx][ny]
                    else:
                        home[cx][cy] = 0
                    cx, cy = nx, ny
                else:
                    k += 1

    return


def dust_diffusion():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    tmp_home = [[0]*C for _ in range(R)]  # 비어있는 임시 home 2중 배열을 만든다.
    for i in range(R):
        for j in range(C):
            if home[i][j] > 0:
                cnt = 0  # 확산된 방의 갯수만큼 빼줘야 되기 때문에 cnt를 세준다.
                for k in range(4):  # 현 위치에서 4방향 탐색
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if home[nx][ny] != -1:
                            # 벽이 아니고, 공기청정기도 아니라면 확산
                            dif_dust = home[i][j]//5
                            tmp_home[nx][ny] += dif_dust
                            cnt += 1

                home[i][j] -= dif_dust*cnt

    # home의 먼지 양에 환산된 tmp_home의 먼지 양을 더해준다.
    for i in range(R):
        for j in range(C):
            if tmp_home[i][j] > 0:
                home[i][j] += tmp_home[i][j]

    return


R, C, T = map(int, input().split())  # 행, 열, 시간
home = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기의 위치, 이 문제에서는 항상 왼쪽 벽에 붙어있다고 가정하는 것 같다.
machine = []
for i in range(R):
    for j in range(C):
        if home[i][j] == -1:
            machine.append([i, j])

for _ in range(T):
    dust_diffusion()
    air_purifier()

result = 0
for i in home:
    result += sum(i)

print(result+2)
