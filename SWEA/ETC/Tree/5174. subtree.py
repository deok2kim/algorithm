T = int(input())
for t in range(1, T+1):
    e, n = map(int, input().split())
    edge_list = list(map(int, input().split()))

    # print(edge_list)
    # 인접 리스트 생성
    adj_list = [[] for _ in range(e + 2)]
    for edge in range(0, len(edge_list), 2):
        adj_list[edge_list[edge]].append(edge_list[edge+1])
    # print(adj)
    visit = [n]
    stack = [n]
    cnt = 0

    while stack:
        current = stack.pop()
        cnt += 1

        for neighbor in adj_list[current]:
            if neighbor not in visit:
                stack.append(neighbor)
                visit.append(neighbor)

    print('#{} {}'.format(t, cnt))
