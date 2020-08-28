from collections import deque

def solution(board):
    answer = 999999
    q = deque()
    q.append((0, 0, 4, 0))

    visited = {  
        (0, 0, 1): 0,  # (x, y, 현재위치(x, y)에서 바라보고 있는 방향): 현재위치까지 오는데 드는 비용
        (0, 0, 3): 0,  # 0, 1, 2, 3 | 상 하 좌 우
    }
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y, d, c = q.popleft()

        # 마지막에 도달 했을 때 최솟값을 결과에 넣는다.
        if x == len(board) - 1 and y == len(board) - 1:
            answer = min(answer, c)

        for k in range(len(dx)):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                nc = c
                if d == 4:  # 맨처음엔 어느방향으로나 올 수 있으므로 직선도로 한다.
                    nc += 100
                elif d <= 1 and k <= 1: # 바라보는 방향과 진행 방향이 세로일 때
                    nc += 100
                elif d >= 2 and k >= 2: # 바라보는 방향과 진행 방향이 가로일 때
                    nc += 100
                else: # 바라보는 방향과 진행 방향이 서로 다를 때 | 코너와 직선이 생기므로 600원
                    nc += 500 + 100
                # 방문한 적이 없거나, 방문한 적이 있어도 기존의 비용보다 지금 온 경로의 비용(nc))가 적다면
                if not visited.get((nx, ny, k)) or visited[(nx, ny, k)] > nc:
                    visited[(nx, ny, k)] = nc  # 배열에 추가하거나, nc를 갱신해 준다.
                    q.append((nx, ny, k, nc))  # 다음 출발 지를 q에 넣어준다.
    
    return answer





print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]))
