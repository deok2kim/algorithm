def solution(n, t, m, timetable):
    answer = ''

    # 분으로 바꾸는 작업 and 정렬
    new_timetable = []
    for time in timetable:
        tmp = int(time[:2]) * 60 + int(time[3:])
        new_timetable.append(tmp)
    new_timetable.sort()

    last_order = 9 * 60 + (n - 1) * t
    # 버스가 한대씩 온다.
    for i in range(n):

        # 막차
        if i == n - 1:
            # 가정 먼저 온 크루가 막차 시간보다 늦게 도착하거나
            # 콘이 탈 수 있는 자리가 있을 때 (남은 크루가 자리보다 적어서)
            # 그러면 막차 도착시간에 간다~
            if new_timetable[0] > last_order or len(new_timetable) < m:
                return f"{last_order // 60:02d}:{last_order % 60:02d}"
            # 위의 경우가 아니라면
            # m번 째 크루보다 1분 일찍와서 자리 뺏기!
            else:
                return f"{(new_timetable[m - 1] - 1) // 60:02d}:{(new_timetable[m - 1] - 1) % 60:02d}"

        # i번째 버스
        for j in range(m):
            bus_time = 9 * 60 + i * t  # i번째 버스 도착 시간
            if new_timetable[0] <= bus_time:  # 크루 도착시간이 더 작으면
                new_timetable.pop(0)  # 크루 탑승
            else:
                break
    return answer


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(1, 1, 1, ["08:00", "08:01", "08:02", "08:03", "08:03", "08:03", "08:02", "08:02"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(10, 1, 1, ["08:00"]))
