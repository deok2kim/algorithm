def solution(n, ladder):
    answer = []

    for i in range(n):
        x, y = 0, i
        while x < len(ladder):
            if y == 0:
                if ladder[x][0] == 1:  # 오른쪽으로
                    y += 1
            elif y == n - 1:
                if ladder[x][n - 2] == 1:
                    y -= 1
            else:
                if ladder[x][y - 1] == 1:
                    y -= 1
                elif ladder[x][y] == 1:
                    y += 1
            x += 1
        answer.append(y + 1)
    return answer


print(solution(4, [[1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0], [1, 0, 0]]))
