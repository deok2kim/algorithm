def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        fibo = [0] * (n+1)
        fibo[1] = 1
        fibo[2] = 2
        for i in range(3, n+1):
            fibo[i] = (fibo[i-1] + fibo[i-2])%1000000007
    # print(fibo)
    answer = fibo[n]
    return answer