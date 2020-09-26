def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n

    while right >= left:
        finish_cnt = 0
        mid = (left + right) // 2
        for time in times:
            finish_cnt += mid // time

        if finish_cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print('답: ', solution(6, [10, 10]))
print('답: ', solution(6, [7, 10]))
print('답: ', solution(5, [1]))
print('답: ', solution(7, [2, 2, 2]))
