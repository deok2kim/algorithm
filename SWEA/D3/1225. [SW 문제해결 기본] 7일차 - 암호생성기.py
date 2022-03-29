T = 10
for t in range(1, T + 1):
    input()
    answer = []
    input_list = list(map(int, input().strip().split(' ')))

    min_num = min(input_list)
    mok = min_num // 15

    # 바로 0 이 되는 문제가 발생 (2번 케이스)
    if mok * 15 == min_num:
        mok -= 1

    input_list = list(map(lambda x: x - 15 * mok, input_list))

    # 뒤로 안보내고 마지막에 바꿔주기
    idx = 0
    cnt = 0
    while True:
        idx %= 8
        cnt = cnt % 5 + 1
        input_list[idx] -= cnt
        # 종료
        if input_list[idx] <= 0:
            # 음수가 된 수를 0으로 바꿔주고
            input_list[idx] = 0
            # 위치를 옮겨준다.
            answer = input_list[idx + 1:] + input_list[:idx + 1]
            print(f'#{t} {" ".join(list(map(str, answer)))}')
            break

        idx += 1