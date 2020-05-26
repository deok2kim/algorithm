def bt(x, y, number):
    if len(number) == 6:
        result.add(number)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < 5 and 0<= ny < 5:
            bt(nx, ny, number+number_map[nx][ny])


number_map = [input().split() for _ in range(5)]
result = set()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(5):
    for j in range(5):
        bt(i, j, '')

print(result)
print(len(result))