import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline


def spring(_field_nutrient, _trees):
    dead_trees = []
    for key, value in _trees.items():
        cx, cy = key
        next_trees = deque()

        for age in value:
            if age <= _field_nutrient[cx][cy]:  # 양분 공급 성공
                next_trees.append(age + 1)
                _field_nutrient[cx][cy] -= age
            else:
                dead_trees.append((cx, cy, age))
        _trees[key] = next_trees
    return dead_trees


def summer(_field_nutrient, _dead_trees):
    for dead_tree in _dead_trees:
        cx, cy, age = dead_tree
        _field_nutrient[cx][cy] += age // 2


def fall(_trees, _N):
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    new_trees = []
    for key, value in _trees.items():
        cx, cy = key
        for age in value:
            if not age % 5:
                for k in range(len(dx)):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if 0 <= nx < _N and 0 <= ny < _N:
                        new_trees.append((nx, ny))

    for tree in new_trees:
        _trees[tree].appendleft(1)


def winter(_field_nutrient, _A):
    for i in range(len(_A)):
        for j in range(len(_A)):
            _field_nutrient[i][j] += _A[i][j]


if __name__ == '__main__':
    N, M, K = map(int, input().split())  # N X N, M 개의 나무, K년 후
    A = [list(map(int, input().split())) for _ in range(N)]  # 각 땅의 영양분 공급 량
    field_nutrient = [[5 for _ in range(N)] for _ in range(N)]  # 실제 땅 - 양분
    trees_dict = defaultdict(deque)

    for _ in range(M):
        x, y, z = map(int, input().split())
        trees_dict[(x - 1, y - 1)].append(z)

    for year in range(K):
        dead_trees = spring(field_nutrient, trees_dict)
        summer(field_nutrient, dead_trees)
        fall(trees_dict, N)
        winter(field_nutrient, A)

    answer = 0
    for key in trees_dict:
        answer += len(trees_dict[key])

    print(answer)



