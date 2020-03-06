def solution(n, t, m, p):
    s = '0123456789ABCDEF'

    def conversion(number, deci):
        q, r = divmod(number, deci)
        n = s[r]
        if q:
            return conversion(q, deci) + n
        else:
            return n

    answer = ''
    total_answer = []
    for i in range(m * t):
        tmp = conversion(i, n)

        tmp = list(tmp)
        for j in tmp:
            j = j.upper()
            total_answer.append(j)

    # print(total_answer)
    for i in range(len(total_answer)):
        if i % m == p - 1:
            answer += total_answer[i]

        if len(answer) == t:
            return answer


# print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))
# print(solution(16, 16, 2, 2))
