def graph(depth, cur):
    # 친구의 친구까지 이므로 depth가 2이면 탐색을 멈춰준다.
    if depth == 2:
        return

    # cur의 친한 친구들은 neighbor을 찾고 friend리스트에 넣어준다.
    for neighbor in adj[cur]:
        friend.add(neighbor)
        # depth를 1증가시키고 친구의 친구를 찾아주기 위해 graph함수를 실행
        graph(depth+1, neighbor)


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    adj = {i: [] for i in range(1, N+1)}

    # 인접리스트 | 방향 없는 그래프
    for i in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    # 초대장을 보내줄 친구들을 담을 리스트 | 중복 X
    friend = set()
    friend.add(1)

    graph(0, 1)
    print('#{} {}'.format(tc, len(friend) - 1))
