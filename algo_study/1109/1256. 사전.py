if __name__ == '__main__':
    N, M, K = map(int, input().split())

    dp = [[0] * (M + 1) for ii in range(N + 1)]


    def get_dp(n, m):
        if n == 0 or m == 0:
            return 1

        # 나중에 값을 구하는 부분
        if dp[n][m] != 0:
            return dp[n][m]

        dp[n][m] = get_dp(n - 1, m) + get_dp(n, m - 1)
        return dp[n][m]


    def func(n, m, k):
        ret = ""
        if n == 0:
            ret += 'z' * m
            return ret
        if m == 0:
            ret += 'a' * n
            return ret

        if get_dp(n - 1, m) > k:
            ret += 'a'
            ret += func(n - 1, m, k)
            return ret
        else:
            ret += 'z'
            ret += func(n, m - 1, k - get_dp(n - 1, m))
            return ret


    if K > get_dp(N, M):
        print(-1)
    else:
        print(func(N, M, K - 1))
