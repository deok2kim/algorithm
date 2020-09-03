import sys
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1  # 시작한 쓰레기 포함
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 1 <= nx < N + 1 and 1 <= ny < M + 1:
                if (nx, ny) in trashSet and (nx, ny) not in visited:
                    cnt += 1
                    q.append((nx, ny))
                    visited.add((nx, ny))
    else:
        answer.append(cnt)


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())

    # set() 을 쓰는 이유
    # if tmp in set(): 이렇게 tmp가 set()에 있는지 없는지 확인할 때 시간복잡도가 O(1)이다.
    # 하지만 if tmp in list: list의 경우 O(n)이다.
    trashSet = set()  # 음식물 셋
    visited = set()  # 방문 체크

    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        trashSet.add((r, c))

    answer = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for trash in trashSet:
        if (trash[0], trash[1]) not in visited:  # 방문하지 않았따면
            visited.add((trash[0], trash[1]))  # 방문 추가
            bfs(trash[0], trash[1])  # BFS GOGO!

    print(max(answer))
