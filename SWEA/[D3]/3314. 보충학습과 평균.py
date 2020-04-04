T = int(input())

for t in range(1, T + 1):
    scores = list(map(int, input().split()))
    result = 0
    for score in scores:
        if score < 40:
            result += 40
        else:
            result += score

    print('#{} {}'.format(t, result//5))
