from _collections import deque

def solution(numbers, hand):
    answer = ''
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    left = '*'  # 왼손의 위치
    right = '#'  # 오른손의 위치
    click = ''  # 누른 손을 누적
    for number in numbers:
        # 왼손 사용
        if number in [1, 4, 7]:
            left = number
            click += 'L'

        # 오른손 사용
        elif number in [3, 6, 9]:
            right = number
            click += 'R'

        # 양손 사용 | 눌러야 할 위치에서 BFS 탐색을 한다.
        else:
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            for i in range(len(keypad)):
                for j in range(len(keypad[0])):
                    if keypad[i][j] == number:  # 눌러야할 번호의 위치를 찾고
                        q = deque()
                        q.append((i, j))
                        visit = [[-1]*len(keypad[0]) for _ in range(len(keypad))]  # 새로운 배열을 만들어 BFS 탐색
                        visit[i][j], left_cnt, right_cnt = 0, 0, 0 # 처음 위치 0, 왼손, 오른손 이동해야 할 거리
                        while q:
                            x, y = q.popleft()
                            for k in range(len(dx)):
                                nx = x + dx[k]
                                ny = y + dy[k]
                                if 0 <= nx < len(keypad) and 0 <= ny < len(keypad[0]):
                                    # 먼저 방문하지 않은 곳일 경우, 방문 위치 = 이전 위치 + 1
                                    if visit[nx][ny] == -1:
                                        visit[nx][ny] = visit[x][y] + 1
                                        q.append((nx, ny))

                                    # 왼손을 만날 경우
                                    if keypad[nx][ny] == left:
                                        left_cnt = visit[nx][ny]

                                    # 오른손을 만날 경우
                                   elif keypad[nx][ny] == right:
                                        right_cnt = visit[nx][ny]

                        # 왼손까지의 거리가 가까운 경우
                        if left_cnt < right_cnt:
                            left = number
                            click += 'L'

                        # 오른손까지의 거리가 가까운 경우
                        elif right_cnt < left_cnt:
                            right = number
                            click += 'R'

                        # 양손 모두 거리가 같은 경우, 왼손잡이인지 오른손잡이인지에 따라 결정한다.
                        else:
                            if hand == 'left':
                                left = number
                                click += 'L'
                            else:
                                right = number
                                click += 'R'

    answer = click
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
