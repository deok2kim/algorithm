def solution(n):
    answer = []

    maps = [[0]*n for _ in range(n)]

    x,y = 0, 0
    cnt = 1
    for i in range(n):
        # 1번째
        if i % 3 == 0:
            while True:
                maps[x][y] = cnt
                cnt += 1
                x += 1
                if x >= n or maps[x][y]:
                    x -= 1
                    y += 1
                    break

        # 2번째
        elif i % 3 == 1:
            while True:
                maps[x][y] = cnt
                cnt += 1
                y += 1
                if y >= n or maps[x][y]:
                    y -= 1
                    y -= 1
                    x -= 1
                    break
        # 3번째
        elif i % 3 == 2:
            while True:
                maps[x][y] = cnt
                cnt += 1
                y -= 1
                x -= 1
                if maps[x][y]:
                    y += 1
                    x += 2
                    break
        for row in maps:
            print(row)
        print()
    for i in range(n):
        for j in range(n):
            if maps[i][j]:
                answer.append(maps[i][j])
    for row in maps:
        print(row)
    return answer

print(solution(4))