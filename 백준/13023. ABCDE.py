from _collections import defaultdict


def dfs(c, depth):
    global answer
    if depth == 4:
        answer = 1
        return

    for naver in adj[c]:
        if not visited[naver]:
            visited[naver] = 1
            dfs(naver, depth + 1)
            visited[naver] = 0


if __name__ == '__main__':
    answer = 0
    N, M = map(int, input().split())  # 사람수, 관계수
    adj = defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        dfs(i, 0)

        if answer == 1:
            break

    print(answer)
