from _collections import deque


# 주변에 지뢰가 하나도 없으면 클릭하고 하나라도 있으면 클릭하지 않고 건너 뛴다.
def clickOrNot(x, y):
    global cnt
    next_target = []
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if mine[nx][ny] == '.':
                next_target.append((nx, ny))
            elif mine[nx][ny] == '*':
                break
    else:
        # 지뢰가 주변에 하나도 없어 else문으로 오게 되면
        if next_target: # 이 때 주변으로 갈 수 있는 경우가 있으면(next_target에 값이 존재하면)
            mine[x][y] = 'o'  # 체크했다는 표시를 해주고
            cnt += 1 # 클릭 횟수를 더해주고
            spread(next_target) # 주변으로 퍼져나간다


def spread(lst):
    q = deque(lst)
    while q:
        x, y = q.popleft()
        mine[x][y] = 'o'  # 위 함수의 경우와 다르게 클릭해서 주변으로 퍼졌으므로 일단 체크가 되고
        next_next_target = []
        for k in range(8):  # 8방향 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if mine[nx][ny] == '.':
                    next_next_target.append((nx, ny))
                elif mine[nx][ny] == '*':
                    break
        else:
            # 주변에 지뢰가 없으면 또 다시 퍼져 나간다.
            spread(next_next_target)


# 클릭해도 퍼져나가지 않는 곳
def restTarget():
    global cnt
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '.':
                cnt += 1


for tc in range(1, 1 + int(input())):
    n = int(input())
    mine = [list(input()) for _ in range(n)]
    cnt = 0
    # 8방향 탐색
    dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]  # 좌상부터 시계방향
    # 클릭 할 수 있는 부분('.')을 찾아서 최초 클릭을 할지 말지 정한다.
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '.':
                clickOrNot(i, j)

    restTarget()
    print('#{} {}'.format(tc, cnt))
