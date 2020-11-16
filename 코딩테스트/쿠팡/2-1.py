import heapq


def solution(n, customers):
    # 각 달별 날짜
    month_day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # 0월0일0시0분0초에 일이 끝난 i번 키오스크
    kiosk_list = [f'00:00:00:00:00:{i:05d}' for i in range(1, n + 1)]
    # print(kiosk_list)

    # 키오스크 리스트를 힙트리구조로 만들기
    heapq.heapify(kiosk_list)

    # 각 키오스크가 일한 횟수 저장
    kiosk_work = [0] * (n + 1)
    for cus in customers:

        # 날짜, 시간, 일할 시간
        day, time, work = cus.split()
        MM, DD = map(int, day.split('/'))
        hh, mm, ss = map(int, time.split(':'))

        # 시간을 초로 바꾼다음
        # 일할 시간을 더해주고
        # 다시 시간 분 초로 바꿈
        total_time = hh * 3600 + mm * 60 + ss
        total_time += int(work) * 60

        # 24시간을 넘어가면 날짜를 1올려주는 것
        if total_time >= 24 * 3600:
            DD += 1
            total_time -= 24 * 3600
        hh = total_time // 3600
        mm = total_time % 3600 // 60
        ss = total_time % 3600 % 60

        # 달의 마지막 날을 넘어가면 다음달 1일로 바꾸기
        if DD > month_day[MM]:
            MM += 1
            DD = 1

        # print(MM, DD, hh, mm, ss)

        # 일할 키오스크 꺼내기
        kiosk = heapq.heappop(kiosk_list)
        no = kiosk.split(':')[-1]

        # 일시키기
        kiosk_work[int(no)] += 1

        # 끝난시간으로 다시 집어넣기
        kiosk = f'{MM:02d}:{DD:02d}:{hh:02d}:{mm:02d}:{ss:02d}:{no}'
        heapq.heappush(kiosk_list, kiosk)

    print(kiosk_work)
    # 가장 일 많이 한 키오스크가 일한 횟수
    answer = max(kiosk_work)
    return answer


print(solution(3,
               ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13",
                "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
print(solution(2, ["02/28 23:59:00 03", "03/01 00:00:00 02", "03/01 00:05:00 01"]))
