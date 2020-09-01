def volume():
    for i in range(1, N + 1):
        for j in range(M + 1):
            print(i, j)
            # 현재 가지고 있는 볼륨(값이 1인 경우)에서만 시작할 수 있다!
            if dp[i - 1][j] == 0:
                continue
            # 볼륨을 올리는 경우
            if j + V[i - 1] <= M:
                dp[i][j + V[i - 1]] = 1
            # 볼륨을 내리는 경우
            if j - V[i - 1] >= 0:
                dp[i][j - V[i - 1]] = 1

            for row in dp:
                print(row)
            print()


def answer():
    # 마지막줄에 볼륨(값이1) 이 있어야 연주가 가능한 것!!! 아니면 -1을 출력
    for i in range(M, -1, -1):
        if dp[-1][i] == 1:
            print(i)
            return
    else:
        print(-1)


if __name__ == "__main__":
    N, S, M = map(int, input().split())
    V = list(map(int, input().split()))
    # 최대볼륨(M)까지 각 노래마다 가능한 볼륨 저장
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    # 0번째 행은 노래 시작전
    # 1번째 행부터 첫 노래 시작
    dp[0][S] = 1
    for row in dp:
        print(row)
    print()

    # 가능한 볼륨 저장 하기
    volume()
    # 마지막 연주 때의 가장 큰 볼륨
    answer()
