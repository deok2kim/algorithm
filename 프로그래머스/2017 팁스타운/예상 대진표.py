import math


def solution(n, a, b):

    while True:
        half = n // 2
        if a <= half < b or b <= half < a:
            cnt = 1
            while True:
                if n // 2 == 1:

                    return cnt
                else:
                    n = n // 2
                    cnt += 1
        elif a > half and b > half:
            a -= half
            b -= half

        else:
            n = n // 2

    answer = cnt
    return answer


print(solution(16, 4, 16))
print(solution(128 , 4, 16))
print(solution(8, 4, 1))
print(solution(16, 1, 4))
print(solution(16, 15, 16))
print(solution(32, 4, 1))
print(solution(4, 4, 1))
