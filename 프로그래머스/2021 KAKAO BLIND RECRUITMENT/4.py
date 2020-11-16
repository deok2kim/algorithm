import heapq


def solution(n, s, a, b, fares):
    answer = 0

    # 인접리스트
    adj = {i + 1: [] for i in range(n)}
    for i in range(len(fares)):
        st, e, c = fares[i]
        adj[st].append([e, c])
        adj[e].append([st, c])

    # for key, value in adj.items():
    #     print(key, value)

    k_list = [0] * (n + 1)
    # print(s,a,b)
    asdf = []
    for start in [s, a, b]:
        mst = [False] * (n + 1)
        pq = []
        kk = [float('inf')] * (n + 1)
        kk[start] = 0
        heapq.heappush(pq, (0, start))
        result = 0

        while pq:
            k, u = heapq.heappop(pq)

            if mst[u]:
                continue

            mst[u] = True
            result += k

            for dest, w in adj[u]:

                if not mst[dest]:
                    kk[dest] = min(k + w, kk[dest])
                    heapq.heappush(pq, (kk[dest], dest))
                    # print(f'내위치: {u}, 현재가중치: {k}')
                    # print(kk)
                    # print()
        # print(result)
        # print('끝')
        asdf.append(kk)
    # print('뭐')
    answer = [0] * (n + 1)
    # print(answer)
    # print(asdf)
    for i in range(len(asdf)):
        for j in range(len(asdf[i])):
            answer[j] += asdf[i][j]
    # print(min(answer))
    return min(answer)


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
