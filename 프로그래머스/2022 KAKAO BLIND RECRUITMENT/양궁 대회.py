def solution(n, info):
    answer = []
    max_diff = 0
    max_info = ''

    def dfs(idx, res, r_score, a_score, tot):
        nonlocal max_diff, max_info
        if idx > 10:
            if tot < n:
                res = res[:-1] + str(int(res[-1]) + n - tot)
            # print(idx, res, r_score, a_score, tot)
            diff = r_score - a_score
            if diff > max_diff:
                max_diff = diff
                max_info = res
                # print(max_diff, res)
            elif diff == max_diff and max_info:
                for i in range(len(res) - 1, -1, -1):
                    if int(res[i]) > int(max_info[i]):
                        max_diff = diff
                        max_info = res
                        # print(max_diff, res)
                        break
                    elif int(res[i]) < int(max_info[i]):
                        break
            return
        for i in range(2):
            if i == 0:
                # 라이언이 점수를 먹는다. 어피치보다 한발 더 쏜다.

                cnt = info[idx] + 1
                if cnt + tot <= n:
                    dfs(idx + 1, res + str(cnt), r_score + 10 - idx, a_score, tot + cnt)
                else:
                    # 화살이 부족해서 어피치가 먹거나 둘다 못먹음.
                    if info[idx] > 0:
                        dfs(idx + 1, res + str(0), r_score, a_score + 10 - idx, tot)
                    else:
                        dfs(idx + 1, res + str(0), r_score, a_score, tot)
            else:
                # 어피치가 점수를 먹는다.
                if info[idx] > 0:
                    dfs(idx + 1, res + str(0), r_score, a_score + 10 - idx, tot)
                else:
                    dfs(idx + 1, res + str(0), r_score, a_score, tot)

    dfs(0, '', 0, 0, 0)
    answer = list(map(int, max_info))
    return answer if answer else [-1]


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))

# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
# print(solution(10, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

print(solution(5, [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
