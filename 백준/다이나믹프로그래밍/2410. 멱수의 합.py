def solution(N):
    nums = [2 ** x for x in range(21)]
    dp = [0] * (N + 1)
    dp[0] = 1
    for num in nums:
        if num <= N:
            for j in range(num, N + 1):
                dp[j] += dp[j - num]
    print(dp[-1] % 1000000000)


if __name__ == "__main__":
    N0 = int(input())
    solution(N0)
