from collections import defaultdict

N, M = map(int, input().split())  # 가수의 수, PD의 수

# (그래프)인접리스트
adj = defaultdict(list)
for i in range(M):
    singers = list(map(int, input().split()))
    for j in range(len(singers) - 1):
        adj[singers[j]].append(singers[j + 1])
for key in adj:
    print(f'{key}: {adj[key]}')

# 진입차수
degree = [0]*(N+1)
for key in adj:
    for singer in adj[key]:
        degree[singer] += 1

print(degree)