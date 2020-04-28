n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] == 1 and graph[i][k] == 1:
                print(i, '->', j, ' -> ', k)
                graph[j][k] = 1
                
# bfs 방법
# for i in graph:
#     print(' '.join(list(map(str, i))))
#
# def bfs(x):
#     visited = [0] * n
#     q = [x]
#     while q:
#         idx = q.pop(0)
#         for i in range(n):
#             if not visited[i]:
#                 if data[idx][i] == 1:
#                     visited[i] = 1
#                     q.append(i)
#     print(' '.join(map(str, visited)))
#
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     bfs(i)
