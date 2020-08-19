for tc in range(1, 1 + int(input())):
    n = int(input())
    v = 0
    s = 0
    for _ in range(n):
        inp = input()
        if ' ' in inp:  # 커맨드가 0이 아니라면 | 즉, 감소와 가속 둘 중 하나라면
            command, velocity = map(int, inp.split())
            if command == 1:
                v += velocity
            elif command == 2:
                v -= velocity

        if v < 0:
            v = 0

        s += v

    print('#{} {}'.format(tc, s))
