def solution(grid):
    answer = []
    N, M = len(grid), len(grid[0])
    visited = [[set() for _ in range(M)] for _ in range(N)]

    # U, D, L, R
    for i in range(N):
        for j in range(M):
            for k in 'UDLR':
                cnt = 0
                while True:
                    if k in visited[i][j]:  # 이미 이동했던 적이 있는지 확인
                        break
                    visited[i][j].add(k)  # 없다면 싸이클 시작
                    cnt += 1

                    # 이동
                    if k == 'U':
                        i -= 1
                        if i < 0:
                            i = N - 1
                    elif k == 'D':
                        i += 1
                        if i == N:
                            i = 0
                    elif k == 'L':
                        j -= 1
                        if j < 0:
                            j = M - 1
                    elif k == 'R':
                        j += 1
                        if j == M:
                            j = 0

                    # 다음 방향 체크
                    if grid[i][j] == 'L':
                        if k == 'U':
                            k = 'L'
                        elif k == 'D':
                            k = 'R'
                        elif k == 'L':
                            k = 'D'
                        elif k == 'R':
                            k = 'U'
                    elif grid[i][j] == 'R':
                        if k == 'U':
                            k = 'R'
                        elif k == 'D':
                            k = 'L'
                        elif k == 'L':
                            k = 'U'
                        elif k == 'R':
                            k = 'D'

                if cnt > 0:
                    answer.append(cnt)

    return sorted(answer)


print(solution(["SL", "LR"]))
