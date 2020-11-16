import sys

input = sys.stdin.readline


def go_tetromino(x, y):
    for tetromino in tetrominos:
        sum_tet = 0
        for _x, _y in tetromino:
            try:
                sum_tet += paper[x + _x][y + _y]
            except IndexError:
                break
        else:
            result.append(sum_tet)


if __name__ == '__main__':
    N, M = map(int, input().split())  # 세로 가로
    paper = [list(map(int, input().split())) for _ in range(N)]
    result = []
    tetrominos = [
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (-1, 2)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (1, 0), (2, 0), (2, -1)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (1, 0), (-1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, -1)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (1, 0), (1, 1), (1, -1)],
        [(0, 0), (1, 0), (2, 0), (1, -1)],
        [(0, 0), (1, 0), (1, 1), (2, 0)]
    ]
    for i in range(N):
        for j in range(M):
            go_tetromino(i, j)

    print(max(result))
