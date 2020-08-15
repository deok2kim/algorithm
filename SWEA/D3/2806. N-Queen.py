def PossibleQueen(y, x):
    # 위쪽
    for i in range(y):
        if chess[y-i-1][x] == 1:
            return False

        if 0 <= x-i-1 < n:
            if chess[y-i-1][x-i-1] == 1:
                return False

        if 0 <= x+i+1 < n:
            if chess[y-i-1][x+i+1] == 1:
                return False

    return True


def queen(idx=0):
    global cnt
    if idx == n:
        cnt += 1
        return

    else:
        for i in range(n):
            if chess[idx][i] == 0 and PossibleQueen(idx, i) is True:
                chess[idx][i] = 1
                queen(idx + 1)
                chess[idx][i] = 0

    return


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cnt = 0
    chess = [[0]*n for _ in range(n)]
    queen()
    print('#{} {}'.format(t, cnt))
