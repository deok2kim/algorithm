def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            tmp = []
            for k in range(4):
                if j != k:
                    tmp.append(land[i - 1][k])

            land[i][j] += max(tmp)

    answer = max(land[len(land) - 1])
    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
print(solution([[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]]))


# 재귀 함수를 이용한 코드. 답은 나오나 재귀가 너무 많이 들어가 제출 시 런타임 에러가 발생
def solution(land):
    answer = 0
    len_land = len(land)
    for _ in land:
        print(_)
    print()

    def dfs(idx, total, imp=None):
        nonlocal answer
        if idx == len_land:
            if total > answer:
                answer = total
            # print(total)
            return

        else:
            for i in range(4):
                if i != imp:
                    total += land[idx][i]
                    dfs(idx + 1, total, i)
                    total -= land[idx][i]

    dfs(0, 0)

    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
print(solution([[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]]))
