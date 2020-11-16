def solution(a):
    answer = 0
    n = len(a)
    # 중복 제거하여 교집합이 될 수 하나씩
    # 인접한 두 원소 중 교집합 원소를 포함하면서 서로 같지 않은 것
    if n == 1:
        return 0

    set_a = set(a)
    numbers_cnt = [0] * (500001)
    for _a in a:
        numbers_cnt[_a] += 1

    for s in set_a:

        if numbers_cnt[s] <= answer // 2:
            continue
        i, j = 0, 1
        cnt = 0
        while j < n:
            if a[i] != a[j] and (a[i] == s or a[j] == s):  # 서로 같지 않고 # 둘 중 하나가 교집합 원소를 포함한다면

                cnt += 2
                i = j + 1
                j += 2
            else:
                j += 1
        answer = max(answer, cnt)

    return answer


print(solution([2, 2]))
