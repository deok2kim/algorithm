    T = int(input())
    for t in range(1, T + 1):
        a, b, c = map(int, input().split())
        result = 0
        if a == b:
            result = c
        elif b == c:
            result = a
        elif a == c:
            result = b

        print('#{} {}'.format(t, result))
