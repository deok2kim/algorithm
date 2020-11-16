def solution(A):
    answer = 0
    A.sort()
    print(A)
    N = len(A)
    for i in range(N):
        answer += abs(A[i] - i - 1)

    return answer


print(solution([1, 2, 1]))
print(solution([2, 1, 4, 4]))
print(solution([6, 2, 3, 5, 6, 3]))
