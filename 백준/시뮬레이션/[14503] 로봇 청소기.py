sero, garo = map(int, input().split())  # n, m
x, y, direction = map(int, input().split())  # r, c, d
field = [list(map(int, input().split())) for _ in range(sero)]

# 0, 1, 2, 3 | 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
while True:
    field[x][y] = 2  # 청소가 끝난 곳
    for k in range(direction-1, direction-1-4, -1):  # 왼쪽 방향부터 탐색하므로 현재방향-1 부터 시작해서 네번 탐색
        k += 4  # 계산하기 쉽게 (-)인덱스를 (+)인덱스로 바꿔준다.
        if k > 3:
            k = k % 4

        nx = x + dx[k]
        ny = y + dy[k]
        # 청소할 곳이 있을 때
        if field[nx][ny] == 0:
            x = nx  # 청소 할 곳으로 이동
            y = ny
            direction = k  # 바라보는 방향을 움직인 방향으로 바꿔준다.
            cnt += 1  # 청소 하고 카운트 + 1
            break

    else:
        # 모든 방향에 더 이상 청소할 곳이 없을 때
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 후진 할 곳이 있을 때
        if field[nx][ny] != 1:
            x = nx
            y = ny
        # 후진 할 곳이 없을 때
        else:
            break
    # for i in field:
    #     print(i)
    # print()
print(cnt)