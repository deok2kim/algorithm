import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

print(max(cnt))

# 간단한 풀이
# N = int(input())
# nums = list(map(int, input().strip().split()))
# dp = [0 for _ in range(1001)]
# for i in range(N):
#     dp[nums[i]] = max(dp[:nums[i]]) + 1
# print(max(dp))
