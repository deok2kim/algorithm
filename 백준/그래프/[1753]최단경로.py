import heapq
# 방향이 있는 그래프 이므로 selected(출발했었는지 확인)가 필요없다
V, E = map(int, input().split())
start = int(input())

# 인접리스트
adj = {i: [] for i in range(1, V+1)}
for _ in range(E):
    s, e, w = map(int, input().split())
    # 방향 그래프
    adj[s].append([e, w])

# dist: 부모인덱스에서 현재인덱스에 도달할 때 생기는 가중치를 담을 배열 | 항상 최소값을 넣어줄 것
INF = float('inf')
dist = [INF] * (V + 1)

# 힙큐는 항상 최솟값을 리턴해준다.
hq = []
heapq.heappush(hq, (0, start))
dist[start] = 0

while hq:
    # 힙큐에서 노드에 대한 가중치와 노드를 뽑는다.
    k, u = heapq.heappop(hq)

    # u에서 갈 수 있는 노드들을 뽑고 | u -> w
    for w, cost in adj[u]:
        # w 가 현재 가지고 있는 가중치보다 u에서 왔을 때의 가중치가 더 적다면
        # w: u에서 갈 수 있는 곳, cost: u -> w 의 가중치
        # dist[u], dist[w]: u, w까지 도달할 때 가중치
        # 내가 지금 w에 도달하는 가중치가, 다른 경로로 w에 도달하는 가중치보다 작다면
        if cost + dist[u] < dist[w]:
            # 가중치를 더 작은 것으로 업데이트, 힙큐에 저장
            dist[w] = cost + dist[u]
            heapq.heappush(hq, (dist[w], w))

# 결과 출력
for i in range(1, V+1):
    if dist[i] != INF:
        print(dist[i])
    else:
        print('INF')
