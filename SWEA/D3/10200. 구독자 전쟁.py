for tc in range(1, 1 + int(input())):
    n, a, b = map(int, input().split())

    max_answer = min(a, b)
    print(a, b)
    min_answer = min(a, b) - (n - max(a, b))
    if min_answer < 0:
        min_answer = 0

    print('#{} {} {}'.format(tc, max_answer, min_answer))
