from itertools import combinations


def solution(n, wires):
    answer = 99999999

    for combi in combinations(wires, n - 2):
        adj = [[] for _ in range(n + 1)]
        for wire in combi:
            a, b = wire
            adj[a].append(b)
            adj[b].append(a)

        visited = [0] * (n + 1)
        stack = [1]
        visited[1] = 1

        while stack:
            c = stack.pop()

            for nei in adj[c]:
                if not visited[nei]:
                    stack.append(nei)
                    visited[nei] = 1

        answer = min(answer, abs(n - visited.count(1) - visited.count(1)))
    return answer


# print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
# print(solution(7, [[1, 2], [2, 7], [3, 4], [4, 5], [6, 7]]))
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
