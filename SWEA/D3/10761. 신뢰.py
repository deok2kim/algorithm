class Robot:
    def __init__(self):
        self.location = 1
        self.time = 0

    def status(self):
        print(f'위치:{self.location}, 시간:{self.time}')


def operate(robot, button):  # 현재위치와 눌러야 되는 버튼
    global time
    # 시간이 같으면 로봇이동
    if time == robot.time:
        robot.time += abs(robot.location - button) + 1
        robot.location = button
        time = robot.time
    else:
        if time - robot.time > abs(robot.location - button):  # 시간이 충분하다면 로봇은 이미 이동했다
            time += 1  # 버튼 누르는 시간
            robot.time = time
            robot.location = button
        else:  # 시간이 충분하지 않았다면 로봇은 시간차이만큼만 이동 후 나머지 이동
            time += abs(robot.location - button) - (time - robot.time) + 1
            robot.location = button
            robot.time = time
    return


for tc in range(int(input())):
    tmp = input().split()
    N = int(tmp[0])
    orders = tmp[1:]
    orange = Robot()
    blue = Robot()
    time = 0
    for i in range(N):
        r, o = orders[i * 2], orders[i * 2 + 1]
        if r == 'O':
            operate(orange, int(o))
        else:
            operate(blue, int(o))

    print(f'#{tc + 1} {time}')
