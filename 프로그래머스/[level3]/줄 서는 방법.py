import math


def solution(n, k):
    answer = []
    numbers = [x + 1 for x in range(n)]

    def cal(N, k):
        if N == 1:
            answer.append(numbers[0])
            return
        all = math.factorial(N)
        sect = all // N
        mok = k // sect
        nmg = k % sect
        if nmg:
            k -= mok * sect
        else:
            mok -= 1
            k -= mok * sect
        select = numbers[mok]
        answer.append(select)
        numbers.remove(select)
        cal(N - 1, k)

    cal(n, k)

    return answer


print(solution(3, 5))
print(solution(5, 25))
