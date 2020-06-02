from _collections import deque


def bfs():
    # 효율을 위해 디큐 사용
    q = deque()
    q.append(1)
    cnt = 0
    # for 문을 쓴 이유는 전체 1번부터 n번 까지 모두 탐색하기 위함
    for i in range(1, n+1):
        # 선택한 번호가 방문하지 않은 상태이면 탐색을 시작
        if visit[i] is False:
            q.append(i)
            visit[i] = True
            cnt += 1

        # 기본적인 bfs와 인접리스트를 활용한 탐색 방법
        while q:
            current = q.popleft()
            for neighbor in adj[current]:
                if not visit[neighbor] and neighbor not in q:
                    q.append(neighbor)
                    visit[neighbor] = True
    else:
        return cnt


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    # 인접리스트 생성
    adj = {i: [] for i in range(n+1)}
    apply = list(map(int, input().split()))
    for i in range(m):
        s, e = apply[i*2], apply[i*2+1]
        adj[s].append(e)
        adj[e].append(s)

    # visit 배열
    visit = [False]*(n+1)

    result = bfs()
    print('#{} {}'.format(tc, result))
