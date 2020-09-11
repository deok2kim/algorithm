def solution(N):
    answer = 0
    dp = [0] * (101)

    for i in range(3):
        dp[i] = i

    for i in range(3, N + 1):
        dp[i] = dp[i-1]+1
        for j in range(i - 2):
            dp[i] = max(dp[i], dp[j] * (i - 2 - j + 1))

        # print(dp)

    answer = dp[N]
    return answer


# solution(int(input()))
print(solution(int(input())))
# print(solution(3))
# print()
# print(solution(7))
# print()
# print(solution(11))
# for i in range(101):
#     print(solution(i))
