def solution(n, m, x, y, queries):
    answer = 0
    x_min, x_max, y_min, y_max = x, x, y, y

    for idx in range(len(queries) - 1, -1, -1):
        direc, dist = queries[idx]
        if direc == 0:  # 좌
            print('좌')
            y_max += dist
            if y_max > m - 1:
                y_max = m - 1
            if y_min != 0:  # 왼쪽 끝일 때
                y_min += dist

        elif direc == 1:  # 우
            print('우')
            y_min -= dist
            if y_min < 0:
                y_min = 0
            if y_max != m - 1:
                y_max -= dist

        elif direc == 2:  # 상
            print('상')
            x_max += dist
            if x_max > n - 1:
                x_max = n - 1
            if x_min != 0:
                x_min += dist

        else:  # 하
            print('하')
            x_min -= dist
            if x_min < 0:
                x_min = 0
            if x_max != n - 1:
                x_max -= dist

        if y_min > m - 1 or y_max < 0 or x_min > n - 1 or x_max < 0:
            return answer
    print(y_min, y_max, x_min, x_max)
    print((y_max - y_min + 1) * (x_max - x_min + 1))
    return answer


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
