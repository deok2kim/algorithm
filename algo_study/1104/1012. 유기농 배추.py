import sys

input = sys.stdin.readline


def find_dummy(x: int, y: int):
    farm[x][y] = 0
    stack = [(x, y)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while stack:
        cx, cy = stack.pop()
        for k in range(len(dx)):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                stack.append((nx, ny))
                farm[nx][ny] = 0


if __name__ == '__main__':
    print()
    for _ in range(int(input())):  # 테스트케이스 개수
        M, N, K = map(int, input().split())  # 가로, 세로, 배추 개수
        farm = [[0] * M for _ in range(N)]

        cabbages = []  # 배추리스트
        for _ in range(K):
            X, Y = map(int, input().split())
            farm[Y][X] = 1  # 배추 심기
            cabbages.append((Y, X))

        answer = 0
        for cabbage in cabbages:
            if farm[cabbage[0]][cabbage[1]] == 1:  # 배추가 심어져있으면
                find_dummy(cabbage[0], cabbage[1])  # 그 배추와 주변 배추 0으로 만들기
                answer += 1  # 더미의 개수 추가

        print(answer)
