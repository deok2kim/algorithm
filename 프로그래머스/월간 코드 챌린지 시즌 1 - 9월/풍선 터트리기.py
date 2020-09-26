import heapq


def solution(a):
    if len(a) < 3:
        return len(a)
    answer = 2
    pq = []
    for i in range(len(a)):
        heapq.heappush(pq, (a[i], i))

    left = heapq.heappop(pq)[1]
    right = heapq.heappop(pq)[1]
    if left > right:
        left, right = right, left

    while pq:
        c = heapq.heappop(pq)[1]
        if c < left:
            answer += 1
            left = c
        elif c > right:
            answer += 1
            right = c

    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
print(solution([-16, 27, 65, -2, 58, -92, -68, -71, -61, -33]))
