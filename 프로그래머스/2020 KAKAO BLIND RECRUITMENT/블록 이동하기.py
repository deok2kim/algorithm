from collections import deque


def solution(board):
    def my_append(t, d):
        # 방문한적이 없을 때 추가해줌
        if t not in visited:
            q.append((t, d))
            visited.add(t)

    n = len(board)

    q = deque()
    visited = set()  # set으로 만들어야 시간복잡도 줄인다
    q.append(((0, 0, 0, 1), 0))
    visited.add((0, 0, 0, 1))
    while q:
        t, d = q.popleft()  # t: 해당 좌표, d: 거리
        x1, y1, x2, y2 = t

        # 가로 도착
        if x1 == n - 1 and x2 == n - 1 and y1 == n - 2 and y2 == n - 1:
            return d
        # 세로 도착
        if x1 == n - 2 and x2 == n - 1 and y1 == n - 1 and y2 == n - 1:
            return d

        d += 1  # 끝에 도착하지 않았으므로 거리를 1 늘림

        # 움직이는 모든 조건
        # 가로 일 때
        if x1 == x2:
            # 오른쪽 이동
            if y2 + 1 < n and board[x2][y2 + 1] == 0:
                t = (x1, y1 + 1, x2, y2 + 1)
                my_append(t, d)
            # 왼쪽 이동
            if y1 - 1 >= 0 and board[x1][y1 - 1] == 0:
                t = (x1, y1 - 1, x2, y2 - 1)
                my_append(t, d)

            # 위로 이동 | 가능하면 오른쪽 위 회전도 가능, 횐쪽 위 회전도 가능
            if x1 - 1 >= 0 and board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
                t = (x1 - 1, y1, x2 - 1, y2)
                my_append(t, d)
                # 오른쪽 위 회전
                t = (x1 - 1, y1 + 1, x2, y2)
                my_append(t, d)
                # 왼쪽 위 회전
                t = (x2 - 1, y2 - 1, x1, y1)
                my_append(t, d)
            # 아래로 이동 | 가능하면 오른쪽 아래 회전도 가능, 왼쪽 아래 회전도 가능
            if x1 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                t = (x1 + 1, y1, x2 + 1, y2)
                my_append(t, d)
                # 오른쪽 아래 회전
                t = (x2, y2, x1 + 1, y1 + 1)
                my_append(t, d)
                # 왼쪽 아래 회전
                t = (x1, y1, x2 + 1, y2 - 1)
                my_append(t, d)

        # 세로 일 때
        elif y1 == y2:
            # 오른쪽 이동
            if y1 + 1 < n and board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
                t = (x1, y1 + 1, x2, y2 + 1)
                my_append(t, d)
                # 오른쪽 아래 회전
                t = (x2, y2, x1 + 1, y1 + 1)
                my_append(t, d)
                # 오른쪽 위 회전
                t = (x1, y1, x2 - 1, y2 + 1)
                my_append(t, d)
            # 왼쪽 이동
            if y1 - 1 >= 0 and board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
                t = (x1, y1 - 1, x2, y2 - 1)
                my_append(t, d)
                # 왼쪽 아래 회전
                t = (x1 + 1, y1 - 1, x2, y2)
                my_append(t, d)
                # 왼쪽 위 회전
                t = (x2 - 1, y2 - 1, x1, y1)
                my_append(t, d)
            # 위로 이동
            if x1 - 1 >= 0 and board[x1 - 1][y1] == 0:
                t = (x1 - 1, y1, x2 - 1, y2)
                my_append(t, d)
            # 아래로 이동
            if x2 + 1 < n and board[x2 + 1][y1] == 0:
                t = (x1 + 1, y1, x2 + 1, y2)
                my_append(t, d)

# print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
# print(solution( [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))

# 7, 21, 11, 33