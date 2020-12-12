# 입력
T = int(input())
Ns = []
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    Ns.append((N, numbers))

# 풀이 - DP
results = []
for tc in range(T):
    N, numbers = Ns[tc]
    # 두번째 부터 끝까지
    # 자신의 앞쪽의 숫자들을 탐색
    # 현재 자신이 몇개의 연속된 증가하는 부분 수열인지 체크
    # 초기화: 자신 혼자 이므로 1로 초기화
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            # 만약 i 의 숫자보다 j 의 숫자가 작으면 증가하는 수열임
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1

    results.append(max(dp))

# 출력
for tc in range(T):
    print(f'#{tc + 1} {results[tc]}')
