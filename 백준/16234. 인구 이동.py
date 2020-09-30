from _collections import deque


def move_population(union_dict):
    for union in union_dict:
        population = union_dict[union]
        for country in union:
            x, y = country
            world[x][y] = population


def find_union(x, y):
    q = deque()
    q.append((x, y))
    union = []
    union.append((x, y))
    total = 0
    count = 0
    while q:
        cx, cy = q.popleft()
        total += world[cx][cy]
        count += 1
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if L <= abs(world[cx][cy] - world[nx][ny]) <= R:
                    union.append((nx, ny))
                    visited.add((nx, ny))
                    q.append((nx, ny))
    if len(union) > 1:
        union_dict[tuple(union)] = total // count


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
if __name__ == '__main__':
    N, L, R = map(int, input().split())
    world = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    while True:
        union_dict = {}
        visited = set()
        for i in range(N):
            for j in range(N):
                if (i, j) not in visited:
                    visited.add((i, j))
                    find_union(i, j)
        if union_dict != {}:
            move_population(union_dict)
            answer += 1
        else:
            break

    print(answer)
