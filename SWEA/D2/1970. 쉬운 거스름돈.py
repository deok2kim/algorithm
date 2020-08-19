coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    change = int(input())
    result = []
    for coin in coins:
        mok = change // coin
        result.append(mok)
        change -= mok*coin

    print(' '.join(list(map(str, result))))
