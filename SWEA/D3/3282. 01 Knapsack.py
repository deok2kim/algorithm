# 입력
T = int(input())
Ns = []
for tc in range(T):
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    Ns.append((N, K, items))

# 풀이
results = []

for tc in range(T):
    N, K, items = Ns[tc]
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, len(dp)):
        v, c = items[i - 1]
        for j in range(1, len(dp[i])):
            # 가방에 아이템이 들어 갈 수 있으면
            if j >= v:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + c)
            else:
                dp[i][j] = dp[i - 1][j]

    results.append(dp[-1][-1])

# 출력
for tc in range(T):
    print(f'#{tc + 1} {results[tc]}')
