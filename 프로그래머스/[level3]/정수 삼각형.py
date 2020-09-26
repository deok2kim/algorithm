def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 < j < i:
                triangle[i][j] += max(triangle[i - 1][j-1], triangle[i-1][j])
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j-1]

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))