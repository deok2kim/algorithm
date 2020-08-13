dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(1, 1+int(input())):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    cnt_list = [0] * (n ** 2 + 1)

    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                low_stack = [(i, j)]
                low_num = maps[i][j]

                high_num = maps[i][j]
                high_stack = [(i, j)]

                maps[i][j] = -10
                # 큰 숫자 찾기
                while high_stack:
                    x, y = high_stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n:
                            if maps[nx][ny] == high_num + 1:
                                high_stack.append((nx,ny))
                                high_num += 1
                                maps[nx][ny] = -10
                                break
                # 작은 숫자 찾기
                while low_stack:
                    x, y = low_stack.pop()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n:
                            if maps[nx][ny] == low_num - 1:
                                low_stack.append((nx,ny))
                                low_num -= 1
                                maps[nx][ny] = -10
                                break

                cnt_list[low_num] = high_num - low_num + 1

    max_cnt = max(cnt_list)
    max_cnt_idx = cnt_list.index(max_cnt)
    print('#{} {} {}'.format(tc, max_cnt_idx, max_cnt))


