def dfs(cnt, result, i, j):
    # print(i, j)
    if cnt == 6:
        result_list.append(result)
        return

    else:
        # 상
        if 0 <= i - 1:
            dfs(cnt + 1, result + field[i-1][j], i - 1, j)
        # 하
        if i + 1 < 4:
            dfs(cnt + 1, result + field[i+1][j], i + 1, j)
        # 좌
        if 0 <= j - 1:
            dfs(cnt + 1, result + field[i][j-1], i, j - 1)
        # 우
        if j + 1 < 4:
            dfs(cnt + 1, result + field[i][j+1], i, j + 1)


for t in range(1, int(input()) + 1):
    field = [list(map(str, input().split())) for _ in range(4)]
    # field = [ input().split() for _ in range(4) ]

    # for i in field:
    #     print(i)

    result_list = []
    for i in range(4):
        for j in range(4):
            if field[i][j] != 0:
                dfs(0, field[i][j], i, j)

    # print(result_list)
    # print(len(result_list))
    # print(set(result_list))
    print('#{} {}'.format(t, len(set(result_list))))