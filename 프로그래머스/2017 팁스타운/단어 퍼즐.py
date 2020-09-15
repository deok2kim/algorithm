def solution2(strs, t):
    dp = {}
    for i in range(len(t)):
        dp[i] = float('inf')

    for i in range(len(t) - 1, -1, -1):
        for k in range(1, 6):
            if t[i:i + k] in strs:
                print(t[i:i + k])
                dp[i] = min(dp.get(i), dp.get(i + k, 0) + 1)
                print(dp)
    return dp.get(0) if dp.get(0) != float('inf') else -1


def solution3(strs, t):
    n = len(t)
    dp = [float('inf')] * n

    for i in range(n - 1, -1, -1):
        for j in range(1, 6):
            if t[i:i + j] in strs:
                print(t[i:i + j], i, i + j)
                if i + j >= n:
                    dp[i] = min(dp[i], + 1)
                else:
                    dp[i] = min(dp[i], dp[i + j] + 1)
                print(dp)
    if dp[0] == float('inf'):
        answer = -1
    else:
        answer = dp[0]

    return answer


def solution(strs, t):
    n = len(t)
    dp = [0] * (n + 1)
    strs = set(strs)  # set을 사용하면 탐색할 때 시간복잡도 O(1)

    for i in range(1, n + 1):
        dp[i] = float('inf')  # i번째 시작시 최댓값으로 바꿔줌(최솟값 비교를 위해)
        for k in range(1, 6):
            # 인덱스 범위 때문에..
            if i - k < 0:
                s = 0
            else:
                s = i - k
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - k] + 1)
    if dp[-1] == float('inf'):
        answer = -1
    else:
        answer = dp[-1]

    return answer


# print(solution(["ab", "na", "n", "a", "bn"],"nabnabn")
# print(solution3(["ba", "na", "n"], "banana"))
print(solution(["ba", "na", "n", "a"], "bananat"))
