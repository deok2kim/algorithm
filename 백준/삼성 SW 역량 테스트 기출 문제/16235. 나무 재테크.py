from _collections import defaultdict
from copy import deepcopy

N, M, K = map(int, input().split())  # NxN, 나무 M개, K년 후
A = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 추가될 양분
trees = defaultdict(list)

ground = [[5] * N for _ in range(N)]
for i in range(M):
    x, y, age = map(int, input().split())
    trees[(x - 1, y - 1)].append(age)

for _ in range(K):
    # 봄 - 나무가 양분 먹기
    # 나이가 어린 나무부터 먹기
    # 자신의 나이만큼 못먹으면 나무는 죽는다.
    dead_tree = []
    for key in trees:
        grow_tree = []
        trees[key].sort()  # 어린나무부터 정렬
        for tree in trees[key]:
            if ground[key[0]][key[1]] >= tree:  # 땅의 양분이 나무의 나이보다 많으면
                # 양분 먹고 나이 +1
                ground[key[0]][key[1]] -= tree
                grow_tree.append(tree + 1)
            else:
                dead_tree.append((key[0], key[1], tree))
        else:
            trees[key] = grow_tree

    # 여름 - 죽은나무 양분으로 바꾸기
    # 죽은 나무의 나이를 2로 나눈 몫만큼 양분추가
    for tree in dead_tree:
        x, y, age = tree
        ground[x][y] += age // 2

    # 가을 - 나무 번식
    # 나무의 나이가 5배수일 경우 인접한 8개의 칸에 나이가 1인 나무 1개씩 생성
    tmp_trees = deepcopy(trees)
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, - 1, -1]
    for key in tmp_trees:
        for tree in tmp_trees[key]:
            if tree % 5 == 0:  # 5배수이면 나무 번식
                for k in range(len(dx)):
                    nx = key[0] + dx[k]
                    ny = key[1] + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        trees[(nx, ny)].append(1)

    # 겨울 - 양분 추가
    # A[r][c] 만큼 양분 추가
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]

# 결과 - 살아남은 나무의 수
total = 0
for key in trees:
    total += len(trees[key])

print(total)
