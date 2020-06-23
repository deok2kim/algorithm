from _collections import deque


def bfs(c, n):
    # n 이 범위내에 존재하며
    # 한번도 방문한 적이 없거나, 방문한 적이 있다면 최소 시간으로 방문했을 때 탐색을 시작
    if 0 <= n < 100002 and (visit[n] == 0 or visit[n] > visit[c] + 1):
        visit[n] = visit[c] + 1
        q.append(n)


#################################################################################
N, K = map(int, input().split())

visit = [0]*100002
result = 0
q = deque()
q.append(N)

# while 문을 돌며 계속 탐색
while q:
    # 현재위치를 꺼내고
    current = q.popleft()

    # 정지 조건: 목표 지점에 도달하면 break로 while문을 빠져나온다. | visit[c]에는 도달 시간이 저장되어있다.
    if current == K:
        result = visit[current]
        break

    # 가능한 경우의수 3가지를 탐색한다.
    bfs(current, current-1)
    bfs(current, current+1)
    bfs(current, current*2)

print(result)

