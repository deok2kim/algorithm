T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())

    for i in range(m + 1):
        A = i
        B = m - i
        if A + 2*B == n:
            break
    print('#{} {} {}'.format(t, A, B))
