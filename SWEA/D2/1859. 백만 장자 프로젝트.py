T = int(input())
for t in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    profit = 0

    while prices:
        # print(prices)
        max_price = max(prices)
        idx = prices.index(max_price)
        for price in prices[:idx]:
            profit += max_price-price

        prices = prices[idx+1:]

    print('#{} {}'.format(t, profit))
