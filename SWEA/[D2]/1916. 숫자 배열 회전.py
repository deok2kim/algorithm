T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    lst = [input().split() for _ in range(n)]

    # 90 도 회전
    lst_90 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(lst[i][j])

        tmp.reverse()
        lst_90.append(tmp)

    # 180 도 회전
    lst_180 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(lst_90[i][j])

        tmp.reverse()
        lst_180.append(tmp)

    # 270 도 회전
    lst_270 = []
    for j in range(n):
        tmp = []
        for i in range(n):
            tmp.append(lst_180[i][j])

        tmp.reverse()
        lst_270.append(tmp)

    for i in range(n):
        print(''.join(list(map(str, lst_90[i]))), ''.join(list(map(str, lst_180[i]))), ''.join(list(map(str, lst_270[i]))))
