def get_axis_per_count(num):
    count = num // 4 * 2
    nmg = num % 4
    if nmg in (3, 2):
        count += 2
    else:
        count += nmg
    return count


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().strip().split())

    answer = 0
    flag = 0
    for i in range(M):
        if flag in (0, 1):
            answer += get_axis_per_count(N)
            flag += 1
        else:
            answer += get_axis_per_count(N - 2)
            flag += 1
        flag %= 4
    print(f'#{test_case} {answer}')
