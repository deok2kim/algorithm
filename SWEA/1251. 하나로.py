'''
4
2
0 0
0 100
1.0
4
0 0 400 400
0 100 0 100
1.0
6
0 0 400 400 1000 2000
0 100 0 100 600 2000
0.3
9
567 5 45674 24 797 29 0 0 0
345352 5464 145346 54764 5875 0 3453 4545 123
0.0005
'''
import heapq

for tc in range(1, 1+int(input())):
    n = int(input())
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    tax = float(input())

    # 인접 리스트
    adj = {i: [] for i in range(n)}
    for s in range(n):
        for e in range(n):
            if s != e:
                adj[s].append([e, (x_location[s]-x_location[e])**2 + (y_location[s]-y_location[e])**2])

    # Key: 가장 큰 값들로 채운다 | 최소 가중치들을 채울 것임
    # mst: visit
    key = [float('inf')] * n
    mst = [False] * n
    pq = []

    # 시작
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0

    while pq:
        # 가중치가 최소인 정점을 뽑는다.
        k, u = heapq.heappop(pq)

        # 이미 방문한 적이 있으면 skip
        if mst[u]:
            continue

        # 아니라면 방문표시와 가중치를 결과에 더해준다.
        mst[u] = True
        result += k

        # dest: 정점 u에서 갈수 있는 곳
        # w: u -> dest 의 가중치
        for dest, w in adj[u]:
            # 그 중 방문한 적이 없고 현재까지 방문했던 가중치보다 작다면
            if not mst[dest] and w < key[dest]:
                # 새로 갱신해준다.
                key[dest] = w
                heapq.heappush(pq, (w, dest))

    print('#{} {}'.format(tc, round(result*tax)))

