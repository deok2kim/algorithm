from copy import deepcopy

def dfs(idx, maps):  # idx : 몇 번째 cctv 인지,
    global min_result
    # cctv 갯수만큼 idx를 점차 늘려나간다. 마지막 cctv의 감시가 끝나면 최소영역을 비교.
    if idx == len(cctv_location):
        value = 0
        for i in range(len(maps)):
            value += maps[i].count('0')
        min_result = min(min_result, value)
        return

    for i in range(len(cctv_direction[idx])):
        next_maps = deepcopy(maps)  # 딥카피를 이용해 기존의 배열을 건드리지 않고 감시할 수 있는 영역을 바꿔준다.
        x, y = cctv_location[idx]
        surveillance(next_maps, x, y, cctv_direction[idx][i])  #
        dfs(idx+1, next_maps)
    return


def surveillance(maps, x, y, direcs):  # cctv 각각의 감시하는 영역
    for direc in direcs:
        nx, ny = x, y
        if direc == 'u':
            k = 0
        elif direc == 'd':
            k = 1
        elif direc == 'l':
            k = 2
        elif direc == 'r':
            k = 3
        while True:
            nx += dx[k]
            ny += dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == '6':
                    break
                elif maps[nx][ny] == '0':
                    maps[nx][ny] = '#'
            else:
                break

    return


def find_cctv():
    cctv_location = []
    cctv_direction = []
    for i in range(n):
        for j in range(m):
            if office[i][j] == '1':  # 1번 cctv
                cctv_location.append((i, j))
                cctv_direction.append(['u', 'd', 'l', 'r'])  # 1번 cctv가 감시할 수 있는 방향의 종류 | up, down, left, right
            elif office[i][j] == '2':
                cctv_location.append((i, j))
                cctv_direction.append(['ud', 'lr'])
            elif office[i][j] == '3':
                cctv_location.append((i, j))
                cctv_direction.append(['ur', 'rd', 'dl', 'lu'])
            elif office[i][j] == '4':
                cctv_location.append((i, j))
                cctv_direction.append(['lur', 'urd', 'rdl', 'dlu'])
            elif office[i][j] == '5':  # 5번 cctv는 상하좌우 모든 방향을 감시할 수 있으므로 경우의 수에 넣지않고 초기에 구역을 설정해준다.
                k = 0
                cx, cy = i, j
                while k < 4:
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if office[nx][ny] == '6':
                            cx, cy = i, j
                            k += 1
                        elif office[nx][ny] == '0':
                            office[nx][ny] = '#'
                            cx, cy = nx, ny
                        else:
                            cx, cy = nx, ny
                    else:
                        cx, cy = i, j
                        k += 1

    return cctv_location, cctv_direction


n, m = map(int, input().split())  # 세로, 가로
office = [input().split() for _ in range(n)]  # 초기 위치
min_result = 64  # 최대 사각지대 수
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cctv_location, cctv_direction = find_cctv()  # CCTV의 위치와, 방향들
dfs(0, office)
print(min_result)
