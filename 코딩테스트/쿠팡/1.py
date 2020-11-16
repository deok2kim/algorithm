def solution(N):
    answer = []

    for k in range(2, 10):
        # k 진수
        print(k)
        number = N
        result = []
        while True:
            mok = number // k
            nmg = number % k
            result.append(nmg)
            if mok < k:
                result.append(mok)
                break
            number = mok
        print(result)

        total = 1
        for r in result:
            if r:
                total *= r
        print(total)
        answer.append((total, k))

    answer.sort(reverse=True)
    return answer


print(solution(10))
print(solution(14))
