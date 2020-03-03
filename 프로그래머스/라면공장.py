import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    possible_supplies = []
    idx = 0

    while stock < k:
        # print(stock)
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(possible_supplies, (-supplies[i], supplies[i]))
            else:
                idx = i
                break
        else:
            idx = i + 1
        # print(possible_supplies)
        stock += heapq.heappop(possible_supplies)[1]
        answer += 1

    return answer


# print(solution(4, [4, 10, 15], [20, 5, 10], 30))
