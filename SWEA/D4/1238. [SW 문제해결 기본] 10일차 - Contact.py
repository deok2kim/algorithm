from _collections import deque


def contact(current_q):
    global result
    # 마지막 연락받은 사람들 중 가장 큰 값
    result = max(current_q)

    # 다음 연락 받을 사람들이 들어갈 리스트
    next_q = deque()

    # 현재 연락받은 사람들이 연락 할 사람들을 찾는 과정
    while current_q:
        c = current_q.pop()
        for neighbor in adj[c]:
            if visited[neighbor] == 0:
                next_q.append(neighbor)
                visited[neighbor] = 1

    # 만약 다음에 연락 받을 사람이 있으면
    if next_q:
        contact(next_q)


for tc in range(1, 11):
    n, start = map(int, input().split())
    # 인접 리스트를 만든다
    adj_list = list(map(int, input().split()))
    adj = {i:[] for i in range(1, 101)}
    for i in range(0, n, 2):
        adj[adj_list[i]].append(adj_list[i+1])

    # 방문 체크 리스트, 결과 값 저장, q
    visited = [0]*101
    visited[start] = 1
    result = 0
    q = deque()
    q.append(start)

    contact(q)
    print('#{} {}'.format(tc, result))
