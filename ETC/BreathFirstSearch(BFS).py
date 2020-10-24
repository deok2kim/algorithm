from collections import deque

# 인접리스트
# 노드: 1,2,3,4,5,6,7
n = 7
adj = {x: [] for x in range(1, n + 1)}
edges = [
    [1, 2],
    [1, 3],
    [2, 4],
    [2, 5],
    [3, 6],
    [3, 7]
]

# 무방향 그래프이므로 반대쪽도 성립
for edge in edges:
    s, e = edge
    adj[s].append(e)
    adj[e].append(s)

print(adj)

# bfs 는 queue를 사용한다. 속도가 빠른데크를 사용
q = deque()
q.append(1)
visited = [False] * (n + 1)  # 각 인덱스 방문한 적이 있는지
visited[1] = True
visited_seq = []
while q:
    c = q.popleft()  # 큐 구조 이므로 가장 앞의원소(제일 처음에 들어온)를 꺼낸다.

    for neighbor in adj[c]:  # c의 이웃 노드(c에서 바로 갈 수 있는 곳)
        if not visited[neighbor]:  # 방문한적이 없으면
            q.append(neighbor)  # 큐에 넣어주고
            visited[neighbor] = True  # 방문 표시

    visited_seq.append(c)  # 여긴 안써줘도 된다. 단지 방문순서를 나타내기 위한 것

print(f'방문순서 {visited_seq}')
