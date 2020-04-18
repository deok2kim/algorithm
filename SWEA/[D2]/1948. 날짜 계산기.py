T = int(input())
for t in range(1, T+1):
    sm, sd, em, ed = map(int, input().split())
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 1 + ed - sd
    for i in range(sm, em):
        result += month[i]
    print('#{} {}'.format(t, result))
