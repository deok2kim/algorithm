for tc in range(int(input())):
    n = int(input())

    stickers = []
    for i in range(2):
        stickers.append(list(map(int, input().split())))

    max_value = [[0]*n for _ in range(2)]

    # print(stickers)
    # print(max_value)

    max_value[0][0] = stickers[0][0]
    max_value[1][0] = stickers[1][0]

    for i in range(1, n):
        if i == 1:
            max_value[0][1] = stickers[1][0] + stickers[0][1]
            max_value[1][1] = stickers[0][0] + stickers[1][1]

        else:
            max_value[0][i] = stickers[0][i] + max(max_value[1][i-1], max_value[1][i-2])
            max_value[1][i] = stickers[1][i] + max(max_value[0][i-1], max_value[0][i-2])

    print(max(max_value[1][n-1], max_value[0][n-1]))