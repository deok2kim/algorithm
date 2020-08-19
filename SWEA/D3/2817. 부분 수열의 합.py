def solution(tot, idx):
    global cnt

    if tot > k:
        return
    elif tot == k:
        cnt += 1
        return

    for i in range(idx, n):
        if visit[i] is False:
            visit[i] = True
            solution(tot + numbers[i], i)
            visit[i] = False


T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    visit = [False]*n
    cnt = 0

    solution(0, 0)
    print('#{} {}'.format(t, cnt))
