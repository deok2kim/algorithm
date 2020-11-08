from sys import stdin
from collections import deque

input = stdin.readline


def move_snake(direc, location):
    # 머리 늘릴 곳 정하기
    cx, cy = location
    nx, ny = 0, 0
    if direc == 'R':
        nx, ny = cx, cy + 1
    elif direc == 'L':
        nx, ny = cx, cy - 1
    elif direc == 'D':
        nx, ny = cx + 1, cy
    elif direc == 'U':
        nx, ny = cx - 1, cy

    # 벽이나 뱀의 몸통에 부딪히지 않을 때
    if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] != 1:
        # 머리 늘리기
        snake.append((nx, ny))

        if maps[nx][ny] != 4:  # 사과가 아니면 꼬리 땡기기
            tx, ty = snake.popleft()
            maps[tx][ty] = 0

        # 맵에 뱀 놓기
        maps[nx][ny] = 1
    else:
        return False
    return True


def change_direction(c_direction, r_direction):
    # 현재방향, 회전방향
    if r_direction == 'L':
        if c_direction == 'R':
            c_direction = 'U'
        elif c_direction == 'L':
            c_direction = 'D'
        elif c_direction == 'D':
            c_direction = 'R'
        elif c_direction == 'U':
            c_direction = 'L'
    if r_direction == 'D':
        if c_direction == 'R':
            c_direction = 'D'
        elif c_direction == 'L':
            c_direction = 'U'
        elif c_direction == 'D':
            c_direction = 'L'
        elif c_direction == 'U':
            c_direction = 'R'
    return c_direction


if __name__ == '__main__':
    N = int(input())  # 판의 크기
    K = int(input())  # 사과의 개수

    # 맵과 사과의 위치와 뱀의 위치 # 사과는 4 뱀은 1
    maps = [[0] * N for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        maps[x - 1][y - 1] = 4
    maps[0][0] = 1

    # 오더
    L = int(input())  # 방향 전환 횟수
    order = [0] * 10000
    for _ in range(L):
        x, c = input().split()  # x: 초, c: 방향 (L 왼쪽,  D 오른쪽) 으로 90도 회전
        order[int(x)] = c

    # 뱀
    snake = deque([(0, 0)])  # 앞쪽 인덱스가 뱀 꼬리, 뒤쪽 인덱스가 뱀 머리
    direction = 'R'  # 방향 R, L, D, U
    second = 0
    while True:
        second += 1
        # 이동하기
        if move_snake(direction, snake[-1]) is False:
            break

        # 정해진 시간초대에 방향 바꾸기
        if order[second]:
            direction = change_direction(direction, order[second])

    print(second)
