def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for puddle in puddles:
        dp[puddle[1]][puddle[0]] = 'X'

    # for row in dp:
    #     print(row)
    # print()

    for i in range(1, 2):
        for j in range(1, m+1):
            if (i == 1 or j == 1) and dp[i][j] == 0:
                dp[i][j] = 1
            else:
                break

    # for row in dp:
    #     print(row)
    # print()

    for j in range(1, 2):
        for i in range(1, n+1):
            if (i == 1 or j == 1) and dp[i][j] == 0:
                dp[i][j] = 1
            elif dp[i][j] == 'X':
                break
    # for row in dp:
    #     print(row)
    # print()

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if dp[i][j] != 'X':
                if type(dp[i - 1][j]) == int:
                    dp[i][j] += dp[i - 1][j]
                if type(dp[i][j - 1]) == int:
                    dp[i][j] += dp[i][j - 1]

                dp[i][j] = dp[i][j]

    # for row in dp:
    #     print(row)
    # print()

    return dp[-1][-1] % 1000000007


print(solution(4, 3, [[2, 2]]))
print(solution(4, 3, [[1, 2], [2,1]]))
# print(solution(100, 50, [[2, 2], [5, 5]]))
print(solution(1, 2, [[1, 1]]))
