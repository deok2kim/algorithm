from _collections import deque


def move(sec, direc):
    global cnt
    for i in range(sec):
        cnt += 1
        nx = snake[0][0] + dx[direc]
        ny = snake[0][1] + dy[direc]

        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                board[snake[-1][0]][snake[-1][1]] = 0
                snake.appendleft((nx, ny))
                snake.pop()

            elif board[nx][ny] == 2:
                board[nx][ny] = 1
                snake.appendleft((nx, ny))

            # 몸에 부딪히면 끝
            else:
                return False

        # 벽에 부딪히면 끝
        else:
            return False


def rotaion(direc):
    global cur_direc
    if direc == 'L':
        cur_direc -= 1
    elif direc == 'D':
        cur_direc += 1

    if cur_direc < 0:
        cur_direc += 4
    elif cur_direc > 3:
        cur_direc %= 4
    return


###############################################################################################
N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
board = [[0]*N for _ in range(N)]  # 보드 판

board[0][0] = 1  # 뱀 놓기
for _ in range(K):  # 사과 놓기
    i, j = map(int, input().split())
    board[i-1][j-1] = 2

L = int(input())  # 뱀의 방향 변환 횟수

change_direcs = [input().split() for _ in range(L)]
change_direcs.append((100, 'S'))  # 방향 바꾸고 한번더 움직이게 하기 위해서 나머지를 넣어준다.

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 우 하 좌 상
cur_direc = 0

cnt = 0
snake = deque()
snake.append((0, 0))

for second, direction in change_direcs:
    c = cnt
    # 움직이기
    if move(int(second) - c, cur_direc) is False:
        break

    # 방향바꾸기
    rotaion(direction)

print(cnt)