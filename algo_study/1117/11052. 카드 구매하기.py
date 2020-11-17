def buy_cards(N, cards):
    dp = [0] * (N + 1)
    dp[1] = cards[0]

    for i in range(2, N + 1):
        for j in range(i // 2 + 1):
            dp[i] = max(cards[i - 1], dp[j] + dp[i - j], dp[i])

    return dp[-1]


if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))

    answer = buy_cards(N, cards)
    print(answer)
