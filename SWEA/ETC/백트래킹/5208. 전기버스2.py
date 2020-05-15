def backt(idx):
    global result, cnt

    if idx >= n-1:
        result = min(result, cnt)
        return

    if cnt > result:
        return

    battery = stop[idx]
    for i in range(idx+battery, idx, -1):
        cnt += 1
        backt(i)
        cnt -= 1

    return


for tc in range(int(input())):
    n, *stop = list(map(int, input().split()))

    result = 100
    cnt = 0
    backt(0)

    print('#{} {}'.format(tc+1, result-1))
