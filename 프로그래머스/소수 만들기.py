from itertools import combinations


def solution(nums):
    answer = 0
    nums_combi = list(combinations(nums, 3))
    for combi in nums_combi:
        combi = sum(combi)
        if combi % 2 == 0:
            continue
        else:
            for i in range(3, combi, 2):
                if combi % i == 0:
                    break
            else:
                answer += 1

    print(nums_combi)

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
