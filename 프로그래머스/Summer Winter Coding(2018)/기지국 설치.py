import math


def solution(n, stations, w):
    answer = 0
    s = 1
    for station in stations:
        cnt = station - w - s
        answer += math.ceil(cnt / (1 + w * 2))
        s = station + w + 1
    else:
        if s <= n:
            cnt = n - s + 1
            answer += math.ceil(cnt / (1 + w * 2))
    return answer


# print(solution(11, [4, 11], 1))
# print(solution(16, [9], 2))
# print(solution(16, [4], 2))
# print(solution(16, [16], 2))
print(solution(16, [3,8,13], 2))
