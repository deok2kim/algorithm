'''
5
1 0 1 0 1
2 0 1 2 0
1 0 0 0 1
1 0 1 0 1
1 0 0 2 0
'''
from itertools import combinations
from _collections import deque
from copy import deepcopy


def bfs(sl, new_room):
    q = deque()
    # 디큐에 시작점 두곳을 넣어주고
    for i in sl:
        q.append(i)
        # 시작점을 3으로 만든다 | 3으로 만든 이유는 2부터하면 다른 2가있기 때문에 헷갈릴 수 있다.
        new_room[i[0]][i[1]] = 3

    # BFS 탐색
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # 지날 수 있는 방을 만났을 때
                if new_room[nx][ny] == 0 or new_room[nx][ny] == 2:
                    q.append((nx, ny))
                    new_room[nx][ny] = new_room[x][y] + 1

                # 한쪽이 움직이지 않고 기다릴 때
                elif new_room[nx][ny] == new_room[x][y]:
                    return new_room[nx][ny] + 1 - 3

                # 동시에 만났을 때
                elif new_room[nx][ny] == new_room[x][y] + 1:
                    return new_room[nx][ny] - 3


n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]

# 시작할 수 있는 점들을 리스트에 담는다.
start_list = []
for i in range(n):
    for j in range(n):
        if room[i][j] == 2:
            start_list.append((i, j))

result = 987654
# 콤비네이션 함수로 시작리스트 중에서 2개를 뽑는다.
for i in combinations(start_list, 2):
    # 기존의 방은 놔두고 딥카피를 이용해 새로운 방을 만들어준다.
    new_room = deepcopy(room)
    tmp_result = bfs(i, new_room)
    result = min(tmp_result, result)

print(result)
