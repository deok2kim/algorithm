def solution(n):
    dp = [0] * (n + 5)
    # 상영 win 1, 창근 win 0
    # 1개 창근 win
    dp[1] = 0
    # 2개 상영 win
    dp[2] = 1
    # 3개 창근 win
    dp[3] = 0
    # 1개 상영 win
    dp[4] = 1

    for i in range(5, n + 1):
        if dp[i - 1] and dp[i - 3] and dp[i - 4]:
            dp[i] = 0
        else:
            dp[i] = 1

    if dp[n] == 1:
        print('SK')
    else:
        print('CY')
    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    solution(n)
