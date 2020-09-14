def solution(N, stages):
    answer = []

    users = [0] * (N + 2)
    n = len(stages)
    for s in stages:
        users[s] += 1

    # print(users)
    result = []
    for i in range(1, N + 1):
        if n:
            result.append((users[i] / n, i))
            n -= users[i]
        else:
            result.append((0,i))

    # print(result)
    result.sort(key=lambda x: (-x[0], x[1]))
    # print(result)

    for stage in result:
        answer.append(stage[1])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(5, [2, 1, 2, 2, 4, 3, 3]))
