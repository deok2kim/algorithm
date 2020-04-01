T = int(input())
for t in range(1, T + 1):
    d, h, m = 11, 11, 11
    D, H, M = map(int, input().split())

    day = D - d
    hour = H - h
    minute = M - m

    result = day*24*60 + hour*60 + minute

    if result < 0:
        result = -1
    print('#{} {}'.format(t, result))
