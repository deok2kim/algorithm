N = int(input())

dp = [0, 1, 1]
for i in range(2, N):
    dp.append(dp[i] + dp[i-1])

print(dp[-1])