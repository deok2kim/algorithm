for tc in range(1, 1+int(input())):
    n = int(input()) # 섬의 갯수
    x = list(map(int, input().split())) # 섬의 x 좌표
    y = list(map(int, input().split())) # 섬의 y 좌표
    E = float(input()) # 세율

    # 인접 행렬 생성
    adj = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            adj[i][j] = ((x[i]-x[j])**2 + (y[i]-y[j])**2)
            adj[j][i] = ((x[i]-x[j])**2 + (y[i]-y[j])**2)

    # for row in adj:
    #     print(row)

    # key 가중치, mst 방문 개념, p 연결 노드
    INF = float('inf')
    key = [INF]*n
    mst = [False]*n
    p = [-1]*n

    # 시작점 선택: 나는 0선택함
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < n:
        # 아직 mst가 아니고 key가 최소인 정점 선택 : u
        minKey = INF
        u = -1
        for i in range(n):
            if not mst[i] and key[i] < minKey:
                minKey = key[i]
                u = i

        # u를 mst로 선택
        mst[u] = True
        result += minKey
        cnt +=1

        # key값을 갱신
        # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 이면 갱신
        for w in range(n):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u # 나한테 찾아오는 친구

    print('#{} {}'.format(tc, round(result*E)))
