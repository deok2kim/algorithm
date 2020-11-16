from itertools import chain


def solution(land, P, Q):
    # 일렬로 세우기
    line = list(chain.from_iterable(land))
    line.sort()
    # print(line)
    n = len(line)

    # 가장 낮은 층으로 편집 (무조건 0이 아니라 가지고 있는 층중에 맨 밑)
    # 가장 낮은 층은 지형이 다 있으므로 그 위의 블록을 모두 제거하면 된다.
    cost = (sum(line) - line[0] * n) * Q
    answer = cost

    # 한층씩 쌓기
    for i in range(1, n):
        if line[i] != line[i - 1]:
            # print(f'cost: {cost}, line[i-1]: {line[i - 1]}, line[i]: {line[i]} ')
            cost = cost + ((line[i] - line[i - 1]) * i * P) - ((line[i] - line[i - 1]) * (n - i) * Q)
            if answer < cost:  # 시간 단축 - 변곡점
                break
            answer = min(answer, cost)
    return answer


# 이분 탐색
# from collections import defaultdict
#
#
# def solution(land, P, Q):
#     answer = 0
#     n = len(land)
#
#     line = defaultdict(int)
#     for i in range(n):
#         for j in range(n):
#             line[land[i][j]] += 1
#
#     # print(line)
#
#     def cal(k):
#         p, q = 0, 0
#         # print(f'i: {k}')
#         for key, value in line.items():
#             if key > k:
#                 q += (key - k) * value
#             elif key < k:
#                 p += (k - key) * value
#
#         # print(f'total: {p * P + q * Q}')
#         return p * P + q * Q
#
#     bottom = min(line)
#     top = max(line)
#     while True:
#         mid = (bottom + top) // 2
#
#         up_val = cal(mid + 1)
#         mid_val = cal(mid)
#         down_val = cal(mid - 1)
#         if mid_val <= up_val and mid_val <= down_val:
#             answer = mid_val
#             break
#         elif down_val < mid_val:
#             top = mid - 1
#         elif up_val < mid_val:
#             bottom = mid + 1
#
#     return answer


print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))
print(solution([[1, 2], [2, 3]], 3, 2))
