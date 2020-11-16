from copy import deepcopy as d
from collections import deque
import random

def solution(cookies, k):
    def bt(res, idx):
        if len(res) == MX:
            result.append(d(res))

        for i in range(idx, -1, -1):
            if dp[idx] == MX and not res or res[-1] > cookies[i]:
                res.appendleft(cookies[i])
                bt(res, i - 1)
                res.popleft()

    result = []
    n = len(cookies)
    dp = [1] * n
    dp2 = [[] for _ in range(n)]
    for i in range(n):
        init = dp[i]
        for j in range(i - 1, -1, -1):
            if cookies[i] > cookies[j]:
                dp[i] = max(dp[j] + init, dp[i])
    MX = max(dp)
    print(dp)

    bt(deque(), n-1)
    result.sort()
    return list(result[k - 1])


print(solution([1, 4, 2, 6, 5, 3], 2))
print(solution([1, 4, 2, 6, 5, 3, 7], 2))

tmp_coo = []
for i in range(100):
    tt = random.randint(0, 10000)
    tmp_coo.append(tt)

print(solution(tmp_coo,3))
