def eratos(n):
    for j in range(n * 2, E + 1, n):
        dp[j] = 1
    return


S, E = map(int, input().split())
dp = [0] * (E + 1)
dp[0], dp[1] = 1, 1
for i in range(2, E + 1):
    if dp[i] == 0:
        eratos(i)

for i in range(S, E + 1):
    if dp[i] == 0:
        print(i)
