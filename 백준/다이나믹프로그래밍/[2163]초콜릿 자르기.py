n, m = map(int, input().split())

dp = [0]*(m+1)

for i in range(1, m+1):
    dp[i] = (n-1) + n*(i-1)

print(dp[m])