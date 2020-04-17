def solution(stones, k):
    answer = 0
    min_people = min(stones)
    max_people = max(stones)

    while max_people - 1 > min_people:
        check = 0
        mid = (min_people + max_people) // 2

        for i in range(len(stones)):
            if stones[i] < mid:
                check += 1
            else:
                check = 0

            if check >= k:
                max_people = mid
                break
        else:
            min_people = mid

    answer = min_people
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
