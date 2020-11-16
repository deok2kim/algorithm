def solution(play_time, adv_time, logs):
    answer = ''

    tmp = list(map(int, play_time.split(':')))
    play_time = tmp[0]*3600 + tmp[1]*60 + tmp[2]
    # print(play_time)

    tmp = list(map(int, adv_time.split(':')))
    adv_time = tmp[0] * 3600 + tmp[1] * 60 + tmp[2]
    # print(adv_time)

    new_logs = [[0,0]]
    for log in logs:
        ttmp = log.split("-")
        log_tmp = []
        for t in ttmp:
            tmp = list(map(int, t.split(':')))
            a = tmp[0] * 3600 + tmp[1] * 60 + tmp[2]
            log_tmp.append(a)
        new_logs.append(log_tmp)

    new_logs.sort()
    # print(new_logs)
    result_list = []
    last_flag = False
    max_end = 0
    max_end_idx = 0
    for j in range(len(new_logs)):
        if last_flag == True:
            break
        start, end = new_logs[j]
        adv_start = start
        adv_end = adv_time + start
        result = 0
        # print('=============================================')
        hh = adv_start // 3600
        mm, ss = (adv_start - hh * 3600) // 60, (adv_start - hh * 3600 ) % 60
        # print(f'{hh}:{mm}:{ss}')
        ehh = adv_end // 3600
        emm, ess = (adv_end - ehh * 3600) // 60, (adv_end - ehh* 3600) % 60
        # print(f'{ehh}:{emm}:{ess}')

        if adv_end > play_time:
            adv_end = play_time
            adv_start = play_time - adv_time
            last_flag = True
        # print('@@@@@@@@@@@@@@@@', adv_start, adv_end)
        for i in range(max_end_idx, len(new_logs)):
            # print('시작')
            hhh = new_logs[i][0] // 3600
            mmm, sss = (new_logs[i][0] - hhh * 3600) // 60, (new_logs[i][0] - hhh* 3600) % 60
            # print(f'{hhh}:{mmm}:{sss}')

            # 내 끝보다 느리면 break
            if new_logs[i][0] > adv_end:
                break


            # 광고 안에 모두 포함
            if new_logs[i][0] >= adv_start and new_logs[i][1] <= adv_end:
                # print('광고안에포함')
                result += new_logs[i][1] - new_logs[i][0]
                if new_logs[i][1] > max_end:
                    max_end = new_logs[i][1]
                    max_end_idx = i
            # 광고보다 큼
            elif new_logs[i][0] <= adv_start and new_logs[i][1] >= adv_end:
                # print('광고보다큼')
                result += adv_time

            # 나보다 빨리시작
            elif adv_start < new_logs[i][1] < adv_end:
                # print('광고보다빨리시작')
                result += new_logs[i][1]-adv_start

            # 나보다 늦게 시작
            elif adv_start < new_logs[i][0] < adv_end:
                # print('광고보다늦게시작')
                result += adv_end-new_logs[i][0]
            # print('resutl: ', result)

        result_list.append([result, adv_start])



    result_list.sort(key=lambda x: (-x[0], x[1]))
    # print(result_list)
    ehh = result_list[0][1] // 3600
    emm, ess = (result_list[0][1] - ehh * 3600) // 60, (result_list[0][1] - ehh * 3600) % 60

    answer = f'{ehh:02}:{emm:02}:{ess:02}'
    return answer

print(solution("50:00:00","45:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))


# print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))