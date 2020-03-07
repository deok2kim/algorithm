from itertools import combinations

for t in range(1, int(input()) + 1):
    N = int(input())
    cook = [list(map(int, input().split())) for _ in range(N)]
    ingredient = [ x for x in range(N)]

    # for i in cook:
    #     print(i)
    # print()

    lst = list(combinations(ingredient, N//2))
    # print(lst)

    result = []
    len_lst = len(lst)
    for i in range(len(lst)//2):
        a = 0
        b = 0
        for j in range(len(lst[i])):
            for k in range(len(lst[i])):
                a += cook[lst[i][j]][lst[i][k]]
                b += cook[lst[len_lst - i - 1][j]][lst[len_lst - i - 1][k]]

        result.append(abs(a-b))


    # print(result)
    print('#{} {}'.format(t, min(result)))


