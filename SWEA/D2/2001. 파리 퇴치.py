T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))

    flies = [ list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum = 0
            for a in range(M):
                for b in range(M):
                    sum += flies[i+a][j+b]
            result.append(sum)

    print('#{} {}'.format(t, max(result)))