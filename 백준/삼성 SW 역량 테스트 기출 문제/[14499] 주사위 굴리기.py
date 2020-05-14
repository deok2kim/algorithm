def move(i, j, direc):
    global x, y
    if direc == 1:  # 동
        if j + 1 < m:
            y = j + 1
    elif direc == 2:  # 서
        if j - 1 >= 0:
            y = j - 1
    elif direc == 3:  # 북
        if i - 1 >= 0:
            x = i - 1
    elif direc == 4:  # 남
        if i + 1 < n:
            x = i + 1
    if i != x or j != y:
        return True
    return False


def rotation(direc):
    if direc == 1:  # 동
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]

    elif direc == 2:  # 서
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]

    elif direc == 3:  # 북
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]

    elif direc == 4:  # 남
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

def change_number():
    # print('xy', x, y)
    if field[x][y] == 0:
        field[x][y] = dice[3][1]
    else:
        dice[3][1] = field[x][y]
        field[x][y] = 0

    print(dice[1][1])


n, m, x, y, k = map(int, input().split())  # 세로 가로 엑스 와이 명령갯수
field = [list(map(int, input().split())) for _ in range(n)]

orders = list(map(int, input().split()))

# 1, 2, 3, 4 : 동 서 북 남
dice = [[0]*3 for _ in range(4)]

for order in range(len(orders)):
    if move(x, y, orders[order]):
        rotation(orders[order])
        change_number()
