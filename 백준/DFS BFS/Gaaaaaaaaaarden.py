from itertools import combinations, permutations
from _collections import deque
from copy import deepcopy

sero, garo, greens, reds = map(int, input().split())
garden = [list(input().split()) for _ in range(sero)]
# 0은 호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴 수 있는 땅을 의미한다.

good_ground_all = []
for i in range(sero):
    for j in range(garo):
        if garden[i][j] == '2':
            good_ground_all.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for c1 in combinations(range(len(good_ground_all)), greens + reds):
    for c2 in combinations(range(reds + greens), greens):

        garden_copy = deepcopy(garden)
        good_q = deque()
        cnt = 0
        for i in range(greens + reds):
            x, y = good_ground_all[c1[i]]
            if i in c2:
                garden_copy[x][y] = ['g', 0]
            else:
                garden_copy[x][y] = ['r', 0]

            good_q.append((x, y))

        # print('before')
        # for i in garden_copy:
        #     print(i)
        # print()

        while good_q:
            x, y = good_q.popleft()
            if garden_copy[x][y] == 'S':
                continue

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < sero and 0 <= ny < garo:
                    if type(garden_copy[nx][ny]) == list:
                        if garden_copy[x][y][0] == 'g':
                            if garden_copy[nx][ny][0] == 'r' and garden_copy[nx][ny][1] == garden_copy[x][y][1] + 1:
                                garden_copy[nx][ny] = 'S'
                                cnt += 1
                        else:
                            if garden_copy[nx][ny][0] == 'g' and garden_copy[nx][ny][1] == garden_copy[x][y][1] + 1:
                                garden_copy[nx][ny] = 'S'
                                cnt += 1

                    else:
                        if garden_copy[nx][ny] == '1' or garden_copy[nx][ny] == '2':
                            good_q.append((nx, ny))
                            garden_copy[nx][ny] = [garden_copy[x][y][0], garden_copy[x][y][1] + 1]

        #     print('ing')
        #     for i in garden_copy:
        #         print(i)
        #     print()
        #
        # print('after')
        # for i in garden_copy:
        #     print(i)
        # print()
        result.append(cnt)

print(max(result))