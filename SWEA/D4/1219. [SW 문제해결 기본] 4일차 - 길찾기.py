for _ in range(1, 11):
    tc, n = map(int, input().split())

    # 인접 리스트를 만든다.
    # {1:[2,3], 2:[4,8]}
    # 1에서 2와 3으로 갈 수 있고, 2에서 4와 8로 갈 수 있다는 의미
    adj_list = list(map(int, input().split()))
    adj = {x:[] for x in range(100)}
    for i in range(0, n*2, 2):
        s = adj_list[i]
        e = adj_list[i+1]
        adj[s].append(e)

    stack = [0]
    # 중복탐색을 막기 위해 visit을 활용
    visit = [0]*(100)
    visit[0] = 1

    answer = 0
    while stack:
        c = stack.pop()
        for neighbor in adj[c]:
            # 끝점을 만나면 길이 있다는 의미이므로 1을 담아주고 while문을 끝내준다.
            if neighbor == 99:
                answer = 1
                break
            if visit[neighbor] == 0:
                stack.append(neighbor)
                visit[neighbor] = 1

    print('#{} {}'.format(tc, answer))
