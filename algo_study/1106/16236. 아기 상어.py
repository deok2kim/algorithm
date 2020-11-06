def find_baby_location():
    location = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 9:
                location.append((i, j))
                maps[i][j] = 0
                return location


def bfs(q: list):
    # print(f'갈 수 있는 위치: {q}')
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    next_q = []
    caught_fish = []
    for cx, cy in q:
        for k in range(len(dx)):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] <= level and visited[nx][ny] == 0:
                next_q.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
                if 0 < maps[nx][ny] < level:
                    caught_fish.append((nx, ny))

    if caught_fish:
        eat_fish(caught_fish)
    elif next_q:
        bfs(next_q)


def eat_fish(caught_fish):
    # print(f'임시로 잡은 물고기: {caught_fish}')
    global eat_fish_cnt, level, move_cnt, check
    caught_fish.sort()
    maps[caught_fish[0][0]][caught_fish[0][1]] = 9
    eat_fish_cnt += 1
    if level == eat_fish_cnt:
        level += 1
        eat_fish_cnt = 0

    move_cnt += visited[caught_fish[0][0]][caught_fish[0][1]] - 1
    check = True


if __name__ == '__main__':
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # for row in maps:
    #     print(row)
    # print()
    level = 2
    eat_fish_cnt = 0
    move_cnt = 0
    check = False
    while True:
        # print('--------------------------------')
        # check = 0
        check = False
        # 아기상어의 위치 찾기
        baby_location = find_baby_location()
        # print(f'현재 물고기 위치: {baby_location}')
        # print(f'물고기 레벨: {level}')
        # 먹을 수 있는 물고기 있는지 탐색하기
        visited = [[0] * N for _ in range(N)]
        visited[baby_location[0][0]][baby_location[0][1]] = 1

        bfs(baby_location)
        # 먹을 수 있는 물고기가 있다면 먹기
        if not check:
            break
        # print(move_cnt)
        # for row in maps:
        #     print(row)
        # print()

    print(move_cnt)
