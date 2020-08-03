for tc in range(1, int(input()) + 1):
    n = int(input())
    names = [input() for _ in range(n)]

    names = list(set(names))
    a = sorted(names, key=lambda x: (len(x), x))

    print('#{}'.format(tc))
    for name in a:
        print(name)