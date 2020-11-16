import heapq

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def solution(n, customers):
    answer = 0
    # 업무 횟수
    work_count = [0] * (n + 1)
    pq = []
    # 키오스크의 조합은
    for i in range(n):
        heapq.heappush(pq, (f'0000000000:{i + 1:05d}'))

    # print(pq)

    for customer in customers:
        # print(customer)
        # 날짜, 시간, 작업시간 파싱
        a = customer.split()
        # print(a)
        month, date = map(int, a[0].split('/'))
        h, m, s = map(int, a[1].split(':'))
        work_time = int(a[2])
        # print(month, date, h, m, s, work_time)

        # 작업 시간 더해주기
        m += work_time

        # 분이 60분 넘어가면 시 1시간 올려주기
        if m >= 60:
            h += 1
            m -= 60

        # 시가 24 넘어가면 날 1 올려주기
        if h >= 24:
            date += 1
            h -= 24

        # 날이 그 달의 날을 넘어가면 월 1 올려주기
        if date > day[month]:
            date -= day[month]
            month += 1

        # print()
        print('끝나는 타임: ', month, date, h, m, s)

        # 다시 문자처럼 합치기
        tmp = f'{month:02}{date:02}{h:02}{m:02}{s:02}'
        # print(tmp)

        # 키오스크 하나 꺼내기
        kiosk = heapq.heappop(pq)
        # print(kiosk)
        id = kiosk.split(':')[1]
        # print(id)
        tmp += f':{id}'
        # print(tmp)
        heapq.heappush(pq, tmp)
        # 업무 횟수 추가
        work_count[int(id)] += 1
        #
        # print()

    # print('------------------------------', work_count)
    return answer


print(solution(3,
               ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13",
                "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
print(solution(2, ["02/28 23:59:00 03", "03/01 00:00:00 02", "03/01 00:05:00 01"]))
