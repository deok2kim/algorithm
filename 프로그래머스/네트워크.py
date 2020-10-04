def solution(n, computers):
    visit = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0:
                stack = [(i, j)]
                visit[i][j], visit[j][i] = 1, 1
                break
    while stack:
        a, b = stack.pop()
        for k in range(n):
            if computers[a][k] == 1 and visit[a][k] == 0:
                stack.append((a, k))
                visit[a][k], visit[k][a] = 1, 1
            print(stack)
