import heapq


def solution(n, works):
    answer = 0

    # 힙큐 만들기!
    pq = []
    for work in works:
        heapq.heappush(pq, -work)

    # n만큼 반복
    for i in range(n):
        print(pq)
        work = heapq.heappop(pq)
        if work == 0:  # 꺼낸 값이 0이면 모든 일이 다 0이므로 종료
            return 0
        heapq.heappush(pq, work+1)  # 한시간 일하고 다시 힙큐에 저장
    print(pq)
    for work in pq:
        answer += work ** 2

    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
print(solution(1, [1]))
print(solution(10, [1,2,3,4,5]))
print(solution(2, [3,4]))
