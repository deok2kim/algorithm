# 시간이 너무 오래걸림;
def backTracking(idx=0, total=100):
    global max_num
    global visit
    if total <= max_num:
        return

    if idx == N:
        max_num = max(max_num, total)
        return

    else:
        for j in range(N):
            if visit[j] is False:
                visit[j] = True
                backTracking(idx+1, total*field[idx][j]*0.01)
                visit[j] = False

    return


for t in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    # 람다 쓰는 방법
    # field = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    visit = [False] * N
    max_num = 0
    # for i in field:
    #     print(i)
    # print()
    backTracking()
    # print(max_num)
    # max_num = max_num * (0.1**(N*2))
    print('#{}'.format(t), end=' ')
    print(format(max_num, '0.6f'))