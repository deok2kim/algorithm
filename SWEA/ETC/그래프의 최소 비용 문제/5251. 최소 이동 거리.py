for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V)}
    # 인접 리스트 만들기 | 방향있는 그래프
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])

    # dist: 최소 가중치를 갱신해줄 배열, selected: visit 배열과 같은 개념
    dist = [float('inf')] * (V+1)
    selected = [False] * (V+1)

    dist[0] = 0
    cnt = 0
    while cnt < V:
        # dist가 최소인 정점 찾기
        min_v = float('inf')
        u = -1
        for i in range(V):
            # 아직 선택하지 않았으면서 비용이 최소인 곳 찾기
            if not selected[i] and dist[i] < min_v:
                min_v = dist[i]
                u = i

        # 결정(방문)
        selected[u] = True

        # 간선완화 w까지 갈 수 있는 최소 비용으로 dist배열을 갱신해 준다.
        for w, cost in adj[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
        cnt += 1

    print('#{} {}'.format(tc, dist[-1]))
    print(dist)
