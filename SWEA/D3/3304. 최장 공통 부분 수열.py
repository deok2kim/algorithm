# 입력
T = int(input())
Ns = [input() for _ in range(T)]

# 풀이 - LCS
results = []
for tc in range(T):
    A, B = Ns[tc].split()
    dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            # 같을 떄
            if B[i - 1] == A[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # 다를 때
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    results.append((dp[-1][-1]))

# 출력
for tc in range(T):
    print(f'#{tc + 1} {results[tc]}')
