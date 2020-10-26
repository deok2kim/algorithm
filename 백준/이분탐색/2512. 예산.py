N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

left = 0
right = max(budgets)
result = 0
while right >= left:
    mid = (left + right) // 2
    answer = 0
    for budget in budgets:
        if budget > mid:
            answer += mid
        else:
            answer += budget

    # answer: 내가 책정한 총 예산, M: 최대 예산
    if answer > M:
        right = mid - 1
    else:
        left = mid + 1
        result = max(result, answer)
print(right)
