def _dp():
    dp = [0] * (target + 1)  # 경우의 수를 업데이트 할 리스트
    dp[0] = 1

    for coin in coins:
        # print('꺼낸 동전: ',coin)
        for i in range(1, target + 1):
            # coin(내가 가진 동전)이 만들 수 있는 금액(i)보다 크지 않을 때
            if i - coin >= 0:
                dp[i] += dp[i - coin]
        # print('dp: ',dp)

    print(dp[-1])


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())  # 동전의 가지 수 <20
        coins = list(map(int, input().split()))  # 동전의 종류
        target = int(input())  # 만들어야 할 금액
        _dp()
