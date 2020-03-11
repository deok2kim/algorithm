def fibonacci(n):
    if n == 0:
        return memo[n]
    elif n == 1:
        return memo[n]

    if memo[n] == 0:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]

memo = [0]*41
memo[1] = 1
for tc in range(int(input())):
    N = int(input())
    fibonacci(N)
    if N == 0 :
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(memo[N-1], memo[N])
