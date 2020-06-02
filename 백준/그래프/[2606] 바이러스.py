from _collections import deque


def bfs(vertex):

    # 속도가 빠른 디큐를 사용해서 BFS 탐색
    q = deque()
    q.append(vertex)
    # 시작점 방문 체크를 True로 해준다음
    visit[vertex] = True
    while q:
        # 큐에 쌓인 노드들 중에서 하나를 꺼내고
        current = q.popleft()
        # 노드에 인접한 이웃들중
        for neighbor in adj[current]:
            # 방문하지 않은 노드를
            if visit[neighbor] is False:
                # q에 쌓고, 방문 체크를 True로 해준다.
                q.append(neighbor)
                visit[neighbor] = True
    return


n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

# 인접 리스트 생성 | 방향없는 그래프
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 방문 배열 사용
visit = [False]*(n+1)
cnt = 0

# 1번부터 시작
bfs(1)

# 결과는 visit 배열에 True의 갯수를 세준다.
print(visit.count(True)-1)
