def average(number_list):
    return sum(number_list) / len(number_list)


for tc in range(1, 1+int(input())):
    n = int(input())
    incomes = list(map(int, input().split()))

    # 평균 구하기
    avg = average(incomes)

    # 평균보다 작은 소득 갯수 세기
    cnt = 0
    for income in incomes:
        if income <= avg:
            cnt += 1

    print('#{} {}'.format(tc, cnt))