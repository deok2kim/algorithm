def solution(n, computers):
    answer = 1
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i != j and computers[i][j] == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)

    vertex = [x for x in range(n)]
    visit = []
    stack = [vertex.pop()]

    while vertex:
        while stack:
            current = stack.pop()
            visit.append(current)
            for neighbor in adj_list[current]:
                if neighbor not in visit:
                    stack.append(neighbor)
                    visit.append(neighbor)
                    vertex.remove(neighbor)

        if vertex:
            stack = [vertex.pop()]
            answer += 1
    # print(answer)
    return answer


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print()
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])