import sys
from _collections import deque

N, M = map(int, input().split())

# 인접 리스트 생성
adj = {x + 1: [] for x in range(N)}
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)

# 베이컨수가 가장 작을 때와 그 사람
b_num = float('inf')
b_people = 0

# BFS 탐색
for i in range(1, N + 1):
    visited = [-1] * (N + 1) # 방문확인과 베이컨수
    q = deque([i])
    visited[i] = 0
    while q:
        c = q.popleft()
        for neighbor in adj[c]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[c] + 1
                q.append(neighbor)

    # 베이컨수가 최소인 사람 구하기
    if sum(visited) + 1 < b_num:
        b_num = sum(visited) + 1
        b_people = i
print(b_people)
