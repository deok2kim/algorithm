T = int(input())


def is_right(grid):
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '#':
                try:
                    if grid[i + 1][j] == grid[i][j + 1] == grid[i + 1][j + 1] == '#':
                        grid[i][j] = grid[i + 1][j] = grid[i][j + 1] = grid[i + 1][j + 1] = '.'
                    else:
                        return 'NO'
                except IndexError:
                    return 'NO'
    return 'YES'


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    print(f'#{test_case} {is_right(arr)}')
