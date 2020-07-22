
def share(idx=0):
    global result
    # 사탕을 다 나눠줬다면 몇종류 씩 가지고 있는지 검사
    if idx == N:
        tot = 0
        for i in candy:
            tot += len(set(i))

        result = max(result, tot)
        return

    # 아직 덜 나눠줬다면, 안나눠준 사탕종류 중에서 나눠준다.
    else:
        for i in range(1, M+1):
            if not visit[i]:
                candy[idx].append(i)
                visit[i] = True
                share(idx+1)
                visit[i] = False
                candy[idx].remove(i)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 어린이 명수, 사탕 종류
    candy = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        candy.append(tmp[1:])

    # 사탕을 줬는지 안줬는지
    visit = [False]*(M+1)

    # 만약 애들보다 사탕종류가 적다면 애들을 사탕종류에 맞게 줄여준다.
    if N > M:
        N = M

    result = 0
    share()
    print('#{} {}'.format(tc, result))