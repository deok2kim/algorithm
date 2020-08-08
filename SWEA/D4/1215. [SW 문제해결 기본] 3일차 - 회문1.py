for tc in range(1, 11):
    n = int(input())
    llst = [list(input()) for _ in range(8)]
    # for row in llst:
    #     print(row)
    cnt = 0
    # 가로 탐색
    for row in llst:  # row: 가로 한줄
        for i in range(0, 8-n+1):
            word = row[i:i+n]
            # print(word)
            a = word[:(n)//2]
            b = word[(n+1)//2:]
            b.reverse()
            # print(a,b)
            if a == b:
                cnt += 1

    # 세로 탐색
    for col in list(zip(*llst)):  # col: 세로 한줄 - 하지만 튜플형태로 나오므로
        for i in range(0, 8-n+1):
            word = list(col)[i:i+n]
            # print(word)
            a = word[:(n)//2]
            b = word[(n+1)//2:]
            b.reverse()
            # print(a,b)
            if a == b:
                cnt += 1

    print('#{} {}'.format(tc, cnt))