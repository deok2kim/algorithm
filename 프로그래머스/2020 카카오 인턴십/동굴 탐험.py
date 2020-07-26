from collections import deque
def solution(n, path, order):
    answer = True
    adj = {n: [] for n in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    # print(precedeA, precedeB)

    visited = [False]*n
    visited[0] = True

    q = deque()
    q.append(0)

    ready = [False]*n

    # 0이 선행이 필요하면 처음부터 접근 불가
    # if precedeB.get(0):
    #     q.clear()   
    #     answer = False

    while q:
        current = q.popleft()

        # 알고보니 아직 못가는 상태
        # if precedeA.get(precedeB.get(current)):
        #     ready[current] = 1
        if current == precedeA.get(precedeB.get(current)):
            ready[current] = 1
        else:
            for neighbor in adj[current]:
                if visited[neighbor] is False:

                    q.append(neighbor)
                    visited[neighbor] = True

                    if precedeA.get(neighbor):  # 선행조건 일 때
                        if ready[precedeA[neighbor]]:  # 이 선행조건을 필요로 하는 친구가 준비상태이면
                            q.append(precedeA[neighbor])  # 출발시킨다
                            visited[precedeA[neighbor]] = True

                        precedeA[neighbor] = 0

    if sum(visited) != n:
        answer = False
    return answer


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	, [[8,5],[6,7],[4,1]]	))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]	, [[4,1],[5,2]]		))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))