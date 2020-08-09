def dfs(number, x, y):
    # 길이가 7이 되면 result에 값을 추가하고 break
    if len(number) == 7:
        result.add(number)
        return

    # 상하좌우 4방향을 탐색
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 리스트의 범위를 벗어나지 않으면
        if 0 <= nx < 4 and 0 <= ny < 4:
            # number에 값을 붙여주고 다음 지점으로 이동하여 재귀탐색
            dfs(number + maps[nx][ny], nx, ny)

    return


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, 1 + int(input())):
    maps = [input().split() for _ in range(4)]

    # 중복이 없기 때문에 set을 사용했다.
    result = set()
    # 시작 지점을 선택
    for i in range(4):
        for j in range(4):
            dfs('', i, j)
    print('#{} {}'.format(tc, len(result)))
