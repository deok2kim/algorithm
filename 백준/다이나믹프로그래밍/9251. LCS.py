def solution(a, b):
    a = ' ' + a
    b = ' ' + b
    an = len(a)
    bn = len(b)

    dp = [[0]*an for _ in range(bn)]
    for i in range(1, bn):
        for j in range(1, an):
            if b[i] == a[j]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        for row in dp:
            print(row)
        print()
    print(dp[-1][-1])
    return


if __name__ == "__main__":
    a0 = input()
    b0 = input()
    solution(a0, b0)
