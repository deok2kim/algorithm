import heapq


def solution(jobs):
    cur_sec = 0  # 현재시간
    pq = []  # 현재 시간에 작업 대기중인 work
    result = []  # 각각의 work 당 작업 시간을 저장
    jobs.sort()  # 작업 투입 시간이 적은 순서대로 정렬
    length_jobs = len(jobs)
    idx = 0  # 작업 투입 개수

    while idx < length_jobs or pq:  # 작업에 모두 투입하고 대기중인 작업도 없으면 종료
        for i in range(idx, len(jobs)):
            if jobs[i][0] <= cur_sec:  # 작업에 투입할 시간이 현재시간보다 적으면 투입!!
                # 힙큐를 쓰기 위해 작업시간과 투입시간의 순서를 바꿔서 넣어줌
                heapq.heappush(pq, [jobs[i][1], jobs[i][0]])
            else:
                idx = i
                break
        else:
            idx = i + 1
        # print('대기중인 작업: ', pq)

        if pq:
            # 작업시간, 투입시간
            work_sec, enter_sec = heapq.heappop(pq)
            # cur_sec-enter_sec: 대기시간
            result.append(work_sec+cur_sec-enter_sec)
            # 작업시간만큼 현재시간 ++
            cur_sec += work_sec

        else:
            cur_sec += 1

    # 결과
    answer = sum(result) // length_jobs
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]	))
print('---------------------------------')
print(solution([[0, 3], [4, 6], [5, 9]]	))