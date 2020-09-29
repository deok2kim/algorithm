def dice_rotation(d):
    if d == 1:  # 동
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 2:  # 서
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 3:  # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif d == 4:  # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    return dice[0]


def move(cx, cy, d):
    if d == 1:  # 동
        cy += 1
    elif d == 2:  # 서
        cy -= 1
    elif d == 3:  # 북
        cx -= 1
    elif d == 4:  # 남
        cx += 1
    return cx, cy


def number_change(cx, cy):
    if maps[cx][cy] == 0:
        maps[cx][cy] = dice[-1]
    else:
        dice[-1] = maps[cx][cy]
        maps[cx][cy] = 0


if __name__ == "__main__":
    # 지도의 크기 N,M
    # 주사위 좌표 x,y
    # 명령의 개수 K
    N, M, x, y, K = map(int, input().split())
    dice = [0, 0, 0, 0, 0, 0]
    maps = [list(map(int, input().split())) for _ in range(N)]
    dice[-1] = maps[x][y]
    orders = list(map(int, input().split()))
    for order in orders:
        x, y = move(x, y, order)
        print(dice_rotation(order))
        number_change(x, y)
