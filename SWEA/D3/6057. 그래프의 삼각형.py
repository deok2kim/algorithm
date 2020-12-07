from _collections import defaultdict

for tc in range(int(input())):
    N, M = map(int, input().split())

    adj = defaultdict(set)
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].add(e)
        adj[e].add(s)

    total = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            for k in range(j + 1, N + 1):
                if i in adj[j] and j in adj[k] and k in adj[i]:
                    total += 1

    print(f'#{tc + 1} {total}')
