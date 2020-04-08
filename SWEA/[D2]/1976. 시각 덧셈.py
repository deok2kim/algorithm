T = int(input())

for t in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    h = h1 + h2
    m = m1 + m2

    time = h*60 + m

    real_h = time//60
    real_m = time%60

    if real_h > 12:
        real_h -= 12

    print('#{} {} {}'.format(t, real_h, real_m))
