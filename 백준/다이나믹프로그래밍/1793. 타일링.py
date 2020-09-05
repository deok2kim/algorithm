import sys


def solution(N):
    answer = 0
    dp = [0] * 251
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N + 1):
        if i % 2 == 0:
            dp[i] = dp[i - 1] * 2 + 1
        else:
            dp[i] = dp[i - 1] * 2 - 1

        # print(dp)
    answer = dp[N]
    return answer


while True:
    try:
        print(solution(int(sys.stdin.readline())))
    except:
        break
