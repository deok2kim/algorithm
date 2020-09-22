def solution(n, money):
    length_money = len(money)
    dp = [[0] * (n + 1) for _ in range(length_money)]

    for i in range(length_money):
        m = money[i]
        dp[i][0] = 1
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - m]

    return dp[-1][-1] % 1000000007


print(solution(5, [1, 2, 5]))
