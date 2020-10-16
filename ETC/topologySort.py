from collections import defaultdict
from collections import deque

V = 7
edges = [
    [1, 2],
    [1, 5],
    [2, 3],
    [3, 4],
    [5, 6],
    [4, 6],
    [6, 7],
]

# 인접 리스트
adj = defaultdict(list)
for edge in edges:
    s, e = edge
    adj[s].append(e)

# print(adj)

# 위상 ( 현재 노드 바로 전 노드가 몇개 인지 ( 나를 지목하고 있는 노드의 개수))
topo = [0] * (V + 1)
for key in adj:
    for node in adj[key]:
        topo[node] += 1

print(f'최초 진입차수: {topo}')

# 진입 차수가 0인 애들을 q에 넣어 준다.
q = deque()
for i in range(1, V + 1):
    if topo[i] == 0:
        q.append(i)

result = []
# 위상 정렬이 완전히 수행되려면 정확히 V개의 노드를 방문해야 한다.
for _ in range(V):
    if not q:
        print('ERROR: 사이클 발생!')
        break

    c = q.popleft()
    result.append(c)
    # c 와 연결 되어있는 간선을 제거 (= 진입차수를 1 뺸다)
    for naver in adj[c]:
        topo[naver] -= 1
        if topo[naver] == 0:
            q.append(naver)

print(f'위상정렬 결과: {result}')
