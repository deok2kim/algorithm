for tc in range(1, 11):
    n = int(input())
    llst = [list(input()) for _ in range(8)]

    cnt = 0
    # 가로 탐색
    for row in llst:  # row: 가로 한줄
        for i in range(0, 8-n+1):
            word = row[i:i+n]
            a = word[:(n+1)//2]
            b = word[(n+1)//2:]
            b.reverse()
            if a == b:
                cnt += 1

    # 세로 탐색
    for col in list(zip(*llst)):  # col: 세로 한줄 - 튜플 형태로 나온다
        for i in range(0, 8-n+1):
            word = list(col)[i:i+n]
            a = word[:(n+1)//2]
            b = word[(n+1)//2:]
            b.reverse()
            if a == b:
                cnt += 1

    print('#{} {}'.format(tc, cnt))