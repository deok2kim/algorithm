def LCS(source, target):
    N1 = len(source) + 1
    N2 = len(target) + 1

    dp = [[0] * N1 for _ in range(N2)]

    for i in range(1, N2):  # 타겟 하나씩
        for j in range(1, N1):  # 쏘스 하나씩
            if target[i - 1] == source[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == '__main__':
    _source = input()
    _target = input()
    print(LCS(_source, _target))
