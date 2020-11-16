def solution(cookie):
    answer = 0
    n = len(cookie)

    for i in range(n - 1):
        left_sum, left_idx = cookie[i], i
        right_sum, right_idx = cookie[i + 1], i + 1

        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                # answer = max(answer, right_sum)

            if left_idx > 0 and left_sum <= right_sum:
                left_idx -= 1
                left_sum += cookie[left_idx]
            elif right_idx < n - 1 and right_sum <= left_sum:
                right_idx += 1
                right_sum += cookie[right_idx]
            else:
                break

    return answer


print(f'답: {solution([1, 1, 2, 3])}')


# 완전탐색
# def solution(cookie):
#     answer = 0
#     n = len(cookie)
#     for i in range(n, 1, -1):
#         for j in range(n - i + 1):
#             # print(j, i)
#             print(cookie[j:j + i])
#             a = cookie[j:j + i]
#             sum_a = sum(a)
#             if sum_a % 2 == 0 and sum_a // 2 > answer:
#                 for k in range(1, i):
#                     # print(f'b{a[:k]}')
#                     # print(f'c{a[k:]}')
#                     b = sum(a[:k])
#                     c = sum(a[k:])
#                     if b == c:
#                         # print(f'이게 왜 {b}?')
#                         answer = max(answer, b)
#     return answer
#
#
# print(f'답: {solution([1, 1, 2, 3])}')
