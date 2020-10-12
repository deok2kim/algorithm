n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    tmp = 0
    for j in range(i - 1, -1, -1):
        if boxes[j] < boxes[i]:
            tmp = max(dp[j], tmp)

    dp[i] += tmp

print(max(dp))
