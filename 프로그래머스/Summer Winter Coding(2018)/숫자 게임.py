def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    for a in A:
        if B[-1] <= a:
            B.remove(B[0])
        else:
            for b in B:
                if b > a:
                    B.remove(b)
                    answer += 1
                    break

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
