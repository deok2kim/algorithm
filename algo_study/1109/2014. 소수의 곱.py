if __name__ == '__main__':
    K, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = []
    max_num = 1
    for num in numbers:
        max_num *= num

    dp = [0] * (max_num + 1)
    dp[1] = 1
    for i in range(2, len(dp)):
        for num in numbers:

            if i / num == i // num and dp[i // num] == 1:
                dp[i] = 1

    cnt = 0
    for i in range(numbers[0], len(dp)):
        if dp[i] == 1:
            cnt += 1
            if cnt == N:
                print(i)
