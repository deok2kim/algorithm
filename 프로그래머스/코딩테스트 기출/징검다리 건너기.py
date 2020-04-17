def solution(stones, k):
    answer = 0
    min_people = min(stones)  # 최소 건널 수 있는 사람 수
    max_people = max(stones) + 1  # 최대로 건널 수 있는 사람 수 + 1
    # +1 을 한 이유는 와일문에 한번이라도 들어가게 하기 위해
    # 만약 최대가 2 최소가 1이면 와일문에 들어가지 않아 결과가 1이 되버린다.

    while max_people - 1 > min_people:  # 최소와 최대의 차이가 1보다 작을 때 까지 반복
        check = 0  # 돌다리를 밟지 못하고 건너 뛰는 횟수
        mid = (min_people + max_people) // 2  # 중간 값

        for i in range(len(stones)):
            if stones[i] < mid:  # 돌다리가 중간 값보다 작아 건너 뛰어야 한다면
                check += 1  # +1
            else:  # 돌다리를 밟고 지나가면 0
                check = 0

            if check >= k:  # 건너 뛴 횟수가 k와 같으면 더 이상 건널 수 없으므로
                max_people = mid  # max 값에 mid 값을 넣어준다
                break
        else:
            min_people = mid  # 무사히 건넌다면 min 값에 mid 값을 넣어준다.

    answer = min_people
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([3, 1, 2, 1, 2], 3))
