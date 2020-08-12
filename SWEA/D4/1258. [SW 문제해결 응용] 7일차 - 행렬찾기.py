from itertools import chain


def findSqure(sx, sy):
    i, j = sx, sy
    while i < n and maps[i][j]:
        i += 1
    else:
        i -= 1

    while j < n and maps[i][j]:
        j += 1
    else:
        j -= 1

    changeZero(sx, i+1, sy, j+1)
    result.append([i-sx+1,j-sy+1])


def changeZero(a,b,c,d):
    # 행 a - b, 열 c - d
    for i in range(a,b):
        for j in range(c,d):
            maps[i][j] = 0


for tc in range(1, 1+int(input())):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    result= []
    for x in range(n):
        for y in range(n):
            if maps[x][y]:
                findSqure(x, y)

    answer = sorted(result, key=lambda x: (x[0]*x[1], x[0]))
    ordered_answer = list(chain.from_iterable(answer))

    print('#{} {} {}'.format(tc, len(answer), ' '.join(list(map(str, ordered_answer)))))