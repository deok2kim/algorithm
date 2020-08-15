T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse=True)

    result = 0

    for i in range(k):
        result += scores[i]

    print('#{} {}'.format(t, result))
    