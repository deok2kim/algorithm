for _ in range(10):
    tc = int(input())
    maze = [input().split() for _ in range(100)]
    x, y = 99, maze[-1].index('2')  # 도착점에서 출발하기로 한다.
    # 좌우 탐색
    while x > 0:
        # print(x, y)
        # 한칸 움직일 때 마다 왼쪽과 오른쪽을 본다. 만약 1이 있으면 그방향으로간다.
        if 0 <= y - 1 < 100 and maze[x][y - 1] == '1':
            # print('좌')
            y -= 1
        elif 0 <= y + 1 < 100 and maze[x][y + 1] == '1':
            # print('우')

            y += 1
        else:
            # print('상')
            x -= 1
        # 지나온 길은 항상 0으로 바꿔준다. 다시돌아가는 것을 방지
        maze[x][y] = 0
    else:
        print('#{} {}'.format(tc, y))
