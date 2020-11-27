from itertools import combinations as cb


def watch():
    for teacher in teacher_list:
        x, y = teacher
        # 상
        nx, ny = x, y
        while nx > 0:
            nx -= 1
            if hallway[nx][ny] == 'S':
                return False

            if hallway[nx][ny] == 'O':
                break
        # 하
        nx, ny = x, y
        while nx < N - 1:
            nx += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 좌
        nx, ny = x, y
        while ny > 0:
            ny -= 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 우
        nx, ny = x, y
        while ny < N - 1:
            ny += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
    return True


if __name__ == '__main__':
    N = int(input())
    hallway = [input().split() for _ in range(N)]

    empty_list = []
    teacher_list = []
    for i in range(N):
        for j in range(N):
            if hallway[i][j] == 'X':
                empty_list.append((i, j))
            elif hallway[i][j] == 'T':
                teacher_list.append((i, j))

    # 벽 3개 뽑기
    for walls in cb(empty_list, 3):

        # 벽 세우기
        for wall in walls:
            x, y = wall
            hallway[x][y] = 'O'
        # 감시하기
        if watch():
            print('YES')
            break
        # 벽 허물기
        for wall in walls:
            x, y = wall
            hallway[x][y] = 'X'
    else:
        print('NO')
