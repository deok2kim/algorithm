def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
