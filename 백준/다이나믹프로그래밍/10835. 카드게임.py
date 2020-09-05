def game():
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if right[j] < left[i]:
                # 오른쪽 버리기 or 왼쪽 버리기 or 둘다 버리기
                dp[i][j] = max(dp[i][j + 1] + right[j], dp[i + 1][j], dp[i + 1][j + 1])
            else:
                # 왼쪽 버리기 or 둘다 버리기
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])

            # for row in dp:
            #     print(row)
            # print()


if __name__ == "__main__":
    N = int(input())

    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    game()

    print(dp[0][0])
