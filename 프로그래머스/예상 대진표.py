def solution(n, a, b):
    answer = 1

    c, d = max(a, b), min(a, b)

    while True:
        if c % 2 == 0 and c - d == 1:
            break

        if c % 2 == 0:
            c = c // 2
        else:
            c = (c + 1) // 2

        if d % 2 == 0:
            d = d // 2
        else:
            d = (d + 1) // 2

        answer += 1

    return answer


print(solution(8, 4, 7))
