import heapq

for tc in range(int(input())):
    V, E = map(int, input().split())
    V += 1  # V : 노드의 마지막 번호 ex) 2이면 노드는 3개이므로 +1해줌;

    # 인접 리스트
    adj = {i: [] for i in range(V)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        adj[e].append([s, c])

    # key : 가장 큰 값들로 채움(최소값을 이용할 것이기 때문) | key는 인덱스번호인 정점에서 갈 수 있는 최소 가중치
    # mst : visit과 비슷한 개념
    # pq : 힙큐 모듈 사용 - heapq.heappop 사용시 최소값이 나온다. - 시간복잡도 good
    key = [float('inf')] * V
    mst = [False] * V
    pq = []

    # 시작 점을 정해주고 | 여기서는 아무 정점이나 정해준다. 시작점에서 시작점으로 가는 key 는 0
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0

    while pq:
        k, u = heapq.heappop(pq)  # 가중치가 최소인 정점을 뽑아주고

        if mst[u]:   # 힙큐에 이미 방문한 정점도 포함되어 있으므로, 이미 방문한 정점이 나오면 스킵!
            continue

        mst[u] = True  # 잘뽑았으면 방문 표시
        result += k  # 결과에 가중치를 더해준다.

        for dest, w in adj[u]:  # u 에서 갈 수 있는 곳을 찾아
            if not mst[dest] and w < key[dest]:  # 아직방문하지 않은 곳이면서 key에 저장된 가중치보다 작은 값이라면
                key[dest] = w  # key값을 갱신
                heapq.heappush(pq, (w, dest))  # 힙큐에 다음 목적지를 저장

    print('#{} {}'.format(tc+1, result))
