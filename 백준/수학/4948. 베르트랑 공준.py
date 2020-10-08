import sys


def eratos(n):
    for j in range(n * 2, 123456 * 2 + 1, n):
        dp[j] = 0


dp = [1] * (123456 * 2 + 1)
dp[0], dp[1] = 0, 0
for i in range(2, 123456 * 2 + 1):
    if dp[i] == 1:
        eratos(i)
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:  # 입력 마지막
        break
    print(sum((dp[N + 1:N * 2 + 1])))
