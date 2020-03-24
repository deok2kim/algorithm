n = int(input())
numbers = [0]
numbers += list(map(int, input().split()))
dp = [0]*(n+1)
dp[1] = numbers[1]
dp[2] = max(numbers[2], dp[1]*2)

for i in range(3, n+1):
    dp[i] = numbers[i]
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[n])
