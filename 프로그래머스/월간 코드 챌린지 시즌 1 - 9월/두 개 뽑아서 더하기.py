from itertools import permutations


def solution(numbers):
    answer = set()

    for i in permutations(numbers, 2):
        answer.add(sum(i))

    answer = sorted(list(answer))
    return answer


print(solution([2, 1, 3, 4, 1]))
