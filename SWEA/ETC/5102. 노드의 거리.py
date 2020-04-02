T = int(input())
for t in range(1, T + 1):
    v, e = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    vertex_list = [x for x in range(1, v+1)]
    adj_list = [[] for _ in range(v+1)]

    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    distance = [0]*(v+1)
    q = [s]
    visit_list = [s]

    while q:
        current = q.pop(0)

        if current == g:
            break

        for neighbor in adj_list[current]:
            if neighbor not in visit_list:
                q.append(neighbor)
                visit_list.append(neighbor)
                distance[neighbor] = distance[current] + 1

    print('#{} {}'.format(t, distance[g]))
