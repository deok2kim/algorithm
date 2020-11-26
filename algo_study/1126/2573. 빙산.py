import sys
from _collections import defaultdict

input = sys.stdin.readline


def melt():
    melting_area = {}  # 녹일 곳
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]  # 방문
    stack = []
    stack.append(iceberg[0])
    selected_iceberg = 0  # 선택된 빙산들 ( 나중에 전체 빙산과 비교해서 한덩어리인지 확인 )
    visited[iceberg[0][0]][iceberg[0][1]] = 1
    while stack:
        x, y = stack.pop()
        selected_iceberg += 1
        melting_cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if arctic[nx][ny] and not visited[nx][ny]:  # 옆이 육지이면 다음 탐색
                stack.append((nx, ny))
                visited[nx][ny] = 1
            elif arctic[nx][ny] == 0:  # 옆이 바다이면 녹이는 카운트
                melting_cnt += 1

        melting_area[(x, y)] = melting_cnt

    # 녹이기
    new_iceberg = []  # 새로운 빙산으로 바꾸기 위해
    for key, value in melting_area.items():
        i, j = key
        arctic[i][j] = max(0, arctic[i][j] - value)
        if arctic[i][j] > 0:
            new_iceberg.append((i, j))

    return selected_iceberg, new_iceberg


if __name__ == '__main__':
    N, M = map(int, input().split())
    arctic = [list(map(int, input().split())) for _ in range(N)]

    # 빙산만 찾기
    iceberg = []
    for i in range(N):
        for j in range(M):
            if arctic[i][j]:
                iceberg.append((i, j))

    answer = 0  # year
    while True:
        # 녹이기
        selected_cnt, new_iceberg = melt()
        # 한덩어리인지
        if selected_cnt != len(iceberg):
            break

        if selected_cnt == 0 or len(new_iceberg) == 0:
            answer = 0
            break
        iceberg = new_iceberg[:]

        answer += 1

    print(answer)
