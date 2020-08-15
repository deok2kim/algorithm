T = int(input())
for t in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    result = 0

    a = w * p
    b = 0
    if w <= r:
        b = q
    else:
        b = q + (w-r)*s

    if a < b:
        result = a
    else:
        result = b
    print('#{} {}'.format(t, result))
