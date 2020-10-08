N = int(input())
numbers = list(map(int, input().split()))

dp = numbers[:]
dp[0] = numbers[0]

# print(f'최초DP: {dp}')
for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

            # print(f'i: {i},j: {j}, DP: {dp}')

# print(dp)
print(max(dp))
