import sys

sys.setrecursionlimit(10 ** 9)


def solution(N, relation, dirname):
    def dfs(cur: str, path: int):
        nonlocal answer
        if not adj[cur]:
            answer = max(answer, path)

        for neighbor in adj[cur]:
            dfs(neighbor, path + dirname[neighbor] + 1)

    answer = 0
    adj = [[] for _ in range(N + 1)]
    for s, e in relation:
        adj[s - 1].append(e - 1)

    for i in range(N):
        dirname[i] = len(dirname[i])

    dfs(0, dirname[0])

    return answer


print(solution(7, [[1, 2], [2, 5], [2, 6], [1, 3], [1, 4], [3, 7]],
               ["root", "abcd", "cs", "hello", "etc", "hello", "solution"]))
