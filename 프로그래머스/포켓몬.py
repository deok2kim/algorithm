def solution(nums):
    pick = len(nums) // 2

    poketmon = set(nums)
    len_poketmon = len(poketmon)

    if len_poketmon > pick:
        answer = pick
    else:
        answer = len_poketmon

    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
