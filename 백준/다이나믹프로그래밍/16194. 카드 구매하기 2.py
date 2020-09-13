if __name__ == "__main__":
    N = int(input())
    cards =[0]
    cards += list(map(int, input().split()))
    dp = [float('inf')] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = cards[i]

        for j in range(1, i):
            dp[i] = min(dp[i], dp[i - j] + dp[j])
        print(dp)
    print(dp[-1])
