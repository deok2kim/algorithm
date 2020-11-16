def solution(s):
    answer = []
    new_s = ''

    cycle_cnt = 0
    zero_cnt = 0
    while True:
        cycle_cnt += 1
        # 0 없애기
        tmp_zero_cnt = 0
        for _s in s:
            if _s == '0':
                tmp_zero_cnt += 1
        zero_cnt += tmp_zero_cnt

        # 길이를 2진법으로 바꾸기
        length = len(s) - tmp_zero_cnt

        # s 초기화 후 2진법 숫자 넣기
        s = ''
        while True:
            mok = length // 2
            nmg = length % 2

            s += str(nmg)
            length = mok
            if length < 2:
                s += str(length)
                s = s[::-1]
                break

        if int(s) == 1:
            break

    answer = [cycle_cnt, zero_cnt]
    return answer


print(solution("110010101001"))
