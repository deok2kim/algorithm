for tc in range(int(input())):
    N = int(input())
    telephone_pole = [tuple(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i == j: continue

            if telephone_pole[i][0] < telephone_pole[j][0] and telephone_pole[i][1] > telephone_pole[j][1]:
                cnt += 1
            elif telephone_pole[i][0] > telephone_pole[j][0] and telephone_pole[i][1] < telephone_pole[j][1]:
                cnt += 1

    print(f'#{tc + 1} {cnt // 2}')
