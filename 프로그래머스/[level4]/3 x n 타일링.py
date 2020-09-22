def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1  # 아무것도 두지 않는 경우도 1가지
    sub = 0
    for i in range(2, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sub * 2
        sub += dp[i - 2]

    answer = dp[n] % 1000000007

    # for i in range(11):
    #     if i % 2 == 0:
    #         print(f'n == {i}: {dp[i]}')
    return answer


print(solution(5000))
