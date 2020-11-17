import sys

input = sys.stdin.readline


def make_curve(x, y, d, g):
    # 좌표로 푸는것이 아니라 규칙을 찾아 진행방향으로 푼다!
    # 진행방향은 지금까지 진행해온 것들을 역순으로 꺼내서 반시계 90도 회전시킨다.
    directions = [d]
    for i in range(g):
        for j in range(len(directions) - 1, -1, -1):
            # 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
            directions.append((directions[j] + 1) % 4)
    # print(directions)

    return directions


def set_coordinates(x, y, directions):
    # 진행방향을 구했으면 좌표를 구한다.
    # 전체 크기는 101 x 101
    # 우, 상, 좌, 하
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    maps[x][y] = 1  # 첫 좌표를 표시 안해주면 고장남
    for k in directions:
        x += dx[k]
        y += dy[k]
        maps[x][y] = 1


def get_square():
    cnt = 0
    for i in range(M - 1):
        for j in range(M - 1):
            # i, j를 기준으로 우, 하, 우하 가 1이면 사각형이다.
            if maps[i][j] and maps[i + 1][j] and maps[i][j + 1] and maps[i + 1][j + 1]:
                cnt += 1
    return cnt


if __name__ == '__main__':
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]

    all_curves = []
    M = 101
    maps = [[0] * M for _ in range(M)]

    for info in infos:
        # 헷갈려서 원래 하던대로 x를 세로, y를 가로로 바꿈
        y, x, d, g = info  # 가로, 세로, 방향, 세대
        directions = make_curve(x, y, d, g)
        set_coordinates(x, y, directions)

        # for rw in maps:
        #     print(rw)
        # print()

    # answer
    answer = get_square()
    print(answer)
