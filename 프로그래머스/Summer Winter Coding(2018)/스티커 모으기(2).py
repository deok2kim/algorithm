def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    # 첫 스티커를 떼는 경우
    dp = [0] * n
    dp[0] = sticker[0]
    dp[1] = 0
    for i in range(2, n - 1):
        dp[i] = max(dp[i - 2], dp[i - 3]) + sticker[i]

    # 첫 스티커를 안 떼는 경우
    dp2 = [0] * (n+1)
    dp2[0] = 0
    for i in range(1, n):
        dp2[i] = max(dp2[i - 2], dp2[i - 3]) + sticker[i]

    answer = max(max(dp), max(dp2))
    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([14]))
print(solution([14,12]))

