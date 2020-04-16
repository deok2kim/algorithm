T = int(input())
for t in range(1, T+1):
    n, m, l = map(int, input().split())
    adj_dict = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        adj_dict[a] = b

    # 노드의 갯수가 짝수일 때
    if len(adj_dict) % 2 == 0:
        for i in range(len(adj_dict)-1, 1, -2):
            adj_dict[i//2] = adj_dict[i] + adj_dict[i-1]

            # 더 이상 찾을 필요가 없으므로
            if i//2 == l:
                break
    # 노드의 갯수가 홀수일 때
    else:
        adj_dict[n//2] = adj_dict[n]
        for i in range(len(adj_dict)-2, 1, -2):
            adj_dict[i // 2] = adj_dict[i] + adj_dict[i - 1]
            # 더 이상 찾을 필요가 없으므로
            if i // 2 == l:
                break

    print('#{} {}'.format(t, adj_dict[l]))
