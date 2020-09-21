import heapq


def solution(food_times, k):
    n = len(food_times)  # 전체길이
    pq = []  # 힙큐 넣을 곳
    for i in range(n):  # 힙큐 넣어줌 ( 음식양, 번호 )
        heapq.heappush(pq, (food_times[i], i + 1))

    pre_food = 0  # 가장 밑바닥
    min_food = pq[0][0]  # 현재 음식중 가장 작은 녀석

    # 사이클 돌면서 k에서 시간을 계속 빼준다.
    while True:
        # 사이클 돌았을 때 k 가 음수가 되면 빼주지 말고 나오자
        if k - (min_food - pre_food) * n < 0:
            break

        # 아니라면 k 빼주고
        k -= (min_food - pre_food) * n

        # 힙큐에서도 그 음식을 빼준다.
        heapq.heappop(pq)
        pre_food = min_food  # 바닥은 방금 그 음식의 양이다.
        n -= 1  # 전체 길이도 하나 빼준다.

        # 만약 다 먹었는데도 k가 남아있다면
        # 음식이 부족한 상태이므로
        if not pq:
            return -1

        # 이것을 나중에 해주는 이유는 위에서 비어있을 경우 인덱스 에러가 나기 때문
        min_food = pq[0][0]

    # 전체 길이보다 남은 초가 더 많을 수 있으므로
    # 초를 길이로 나눈 나머지가 답이다.
    idx = k % n
    # 다시 번호 순으로 정렬 해주고
    pq.sort(key=lambda x: x[1])
    answer = pq[idx][1]
    return answer


print(solution([3, 1, 2], 5))
# print(solution([3, 1,  3, 5, 2, 2,6], 14))

# print(solution([3, 1,  3, 5, 2, 2,6], 15))
# print(solution([3, 1,  3, 5, 2, 2,6], 16))
# print(solution([3, 1,  3, 5, 2, 2,6], 17))

print(solution([3, 1, 1, 3, 5, 2, 2, ], 14))
print(solution([3, 1, 1, 3, 5, 2, 2, ], 15))
print(solution([3, 1, 1, 3, 5, 2, 2, ], 16))
print(solution([3, 1, 1, 3, 5, 2, 2, ], 17))
print(solution([3, 1, 1, 3, 6, 2, 2, ], 17))
print(solution([3, 1, 1, 3, 5, 2, 2, ], 18))
