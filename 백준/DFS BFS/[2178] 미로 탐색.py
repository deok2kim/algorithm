from _collections import deque


def bfs(lst, start):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = deque()  # 효율을 위해 deque를 사용
    q.append(start)
    lst[start[0]][start[1]] = 1  # 시작점을 1로 바꿔준다.

    # 모든 지점을 인접한 한칸씩 탐색하기 위해 BFS
    while q:
        x, y = q.popleft()  # q에서 한 지점을 꺼내고
        for k in range(len(dx)):  # 4방향 탐색을 한다.
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < len(lst) and 0 <= ny < len(lst[0]):  # 인덱스를 벗어나는 것을 방지
                if lst[nx][ny] == '1':  # 이동할 수 있는 칸('1')이면
                    lst[nx][ny] = lst[x][y] + 1  # 한칸 이동이므로 이전 칸 +1
                    q.append((nx, ny))

    return lst[-1][-1]


#####################################################################
N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
print(bfs(maze, (0, 0)))
