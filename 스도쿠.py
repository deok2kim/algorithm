def check(cx, cy):
    # 가로 체크
    cnt = 0
    num_list = set()
    for j in range(9):
        if puzzle[cx][j] != 0:
            cnt += 1
            num_list.add(puzzle[cx][j])

    if cnt != len(num_list):
        return False

    # 세로 체크
    cnt = 0
    num_list = set()
    for i in range(9):
        if puzzle[i][cy] != 0:
            cnt += 1
            num_list.add(puzzle[i][cy])

    if cnt != len(num_list):
        return False

    # 네모 체크
    cnt = 0
    num_list = set()
    x = cx // 3
    y = cy // 3
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if puzzle[i][j] != 0:
                cnt += 1
                num_list.add(puzzle[i][j])

    if cnt != len(num_list):
        return False

    return True


for tc in range(1, int(input())+1):
    n = int(input())
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    play = [map(int, input().split()) for _ in range(n)]
    result = 0
    for i in range(n):
        x, y, num = play[i]
        # 퍼즐에 값을 입력하고
        puzzle[x][y] = num
        # 체크를 해준다
        # False이면 그 판은 무효로 하고 게임은 끝
        if not check(x, y):
            result = i
            break
    else:
        result = i + 1

    print('#{} {}'.format(tc, result))
