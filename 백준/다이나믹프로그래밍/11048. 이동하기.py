N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

# 가장 윗줄과 가장 왼쪽줄도 비교를 해줘야 하기 때문에 한칸씩 더해서 만들어준다.
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = maze[i - 1][j - 1] + max(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

print(dp[-1][-1])
