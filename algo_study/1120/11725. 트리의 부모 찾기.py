import sys
from collections import deque

input = sys.stdin.readline


def main(n, edges):
    adj = [[] for _ in range(n + 1)]
    for edge in edges:
        a, b = edge
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * (n + 1)  # 방문 확인 및 부모 저장
    q = deque([1])  # 1이 루트
    visited[1] = 1

    while q:
        c = q.popleft()
        for nei in adj[c]:
            if not visited[nei]:
                q.append(nei)
                visited[nei] = c

    print('\n'.join(list(map(str, visited[2:]))))
    return


if __name__ == '__main__':
    N = int(input())
    EDGES = [list(map(int, input().split())) for _ in range(N - 1)]
    main(N, EDGES)
