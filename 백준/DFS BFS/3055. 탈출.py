def flood(w):
    new_water = []
    for x, y in w:
        for k in range(len(dx)):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if forest[nx][ny] == '.' or type(forest[nx][ny]) == int:
                    forest[nx][ny] = '*'
                    new_water.append((nx, ny))
    return new_water


def move_hedgehog(h):
    new_hedgehog = []
    for x, y in h:
        if forest[x][y] != '*':
            for k in range(len(dx)):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if forest[nx][ny] == 'D':
                        forest[nx][ny] = forest[x][y] + 1
                        return 'finish'
                    if forest[nx][ny] == '.':
                        forest[nx][ny] = forest[x][y] + 1
                        new_hedgehog.append((nx, ny))
    return new_hedgehog


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
if __name__ == '__main__':
    R, C = map(int, input().split())
    forest = [list(input()) for _ in range(R)]

    water = []
    hedgehog = []
    cave = []
    for i in range(R):
        for j in range(C):
            if forest[i][j] == '*':
                water.append((i, j))
            elif forest[i][j] == 'S':
                forest[i][j] = 0
                hedgehog.append((i, j))
            elif forest[i][j] == 'D':
                cave = [i, j]

    while hedgehog:
        hedgehog = move_hedgehog(hedgehog)
        if hedgehog == 'finish':
            print(forest[cave[0]][cave[1]])
            break
        water = flood(water)
    else:
        print('KAKTUS')
