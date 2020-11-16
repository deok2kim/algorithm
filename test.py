def s():
    s1, s2 = input(), input()
    dp = [0] * 1000
    for i in range(len(s1)):
        max_dp = 0
        for j in range(len(s2)):
            if max_dp < dp[j]:
                max_dp = dp[j]
            elif s1[i] == s2[j]:
                dp[j] = max_dp + 1

            print(dp)
s()